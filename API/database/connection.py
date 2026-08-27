import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path


DEFAULT_PATH = Path(__file__).resolve().parent.parent / "wall_of_respect.db"
SEED_PATH = Path(__file__).resolve().parent / "seed.sql"
SEED_VERSION = "historical-data-v6-valid-role-json"
ADMIN_ACCESS = '{"add_user":"Yes","edit_user":"Yes","user_page":"Yes","add_role":"Yes","edit_role":"Yes","role_page":"Yes","add_assc":"Yes","edit_assc":"Yes","assc_page":"Yes","add_camp":"Yes","edit_camp":"Yes","camp_page":"Yes"}'


SCHEMA = """
CREATE TABLE IF NOT EXISTS app_metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS roles(
  id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL,
  access_level TEXT NOT NULL, status INTEGER NOT NULL DEFAULT 1,
  added_at TEXT NOT NULL DEFAULT CURRENT_DATE, added_by INTEGER,
  updated_at TEXT NOT NULL DEFAULT CURRENT_DATE, updated_by INTEGER);
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
  user_name TEXT UNIQUE NOT NULL, img_path TEXT, email TEXT UNIQUE NOT NULL,
  pswd TEXT NOT NULL, status INTEGER NOT NULL DEFAULT 1, role_id INTEGER NOT NULL,
  added_at TEXT NOT NULL DEFAULT CURRENT_DATE, added_by INTEGER,
  updated_at TEXT NOT NULL DEFAULT CURRENT_DATE, updated_by INTEGER,
  FOREIGN KEY(role_id) REFERENCES roles(id));
CREATE TABLE IF NOT EXISTS campaigns(
  id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL,
  status INTEGER NOT NULL DEFAULT 1, added_at TEXT NOT NULL DEFAULT CURRENT_DATE,
  added_by INTEGER, updated_at TEXT NOT NULL DEFAULT CURRENT_DATE, updated_by INTEGER);
CREATE TABLE IF NOT EXISTS associates(
  id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL,
  designation TEXT NOT NULL, description TEXT, moti_quote TEXT, img_path TEXT,
  campaign_id INTEGER NOT NULL, status INTEGER NOT NULL DEFAULT 1,
  added_at TEXT NOT NULL DEFAULT CURRENT_DATE, added_by INTEGER,
  updated_at TEXT NOT NULL DEFAULT CURRENT_DATE, updated_by INTEGER,
  FOREIGN KEY(campaign_id) REFERENCES campaigns(id));
"""


LEGACY_SCHEMA = """
CREATE TABLE roles(ID INTEGER PRIMARY KEY,Name TEXT,Access_level TEXT,Status INTEGER,Added_at TEXT,Added_by INTEGER,Updated_at TEXT,Updated_by INTEGER);
CREATE TABLE users(ID INTEGER PRIMARY KEY,Name TEXT,User_name TEXT,Img_path TEXT,Email TEXT,Pswd TEXT,Status INTEGER);
CREATE TABLE users_log(ID INTEGER PRIMARY KEY,User_name TEXT,Role INTEGER,Added_at TEXT,Added_by INTEGER,Updated_at TEXT,Updated_by INTEGER);
CREATE TABLE campaign(ID INTEGER PRIMARY KEY,Name TEXT,Status INTEGER,Added_at TEXT,Added_by INTEGER,Updated_at TEXT,Updated_by INTEGER);
CREATE TABLE associates_info(ID INTEGER PRIMARY KEY,Name TEXT,Designation TEXT,Description TEXT,moti_quote TEXT,Img_path TEXT,Campaign_id INTEGER,Status INTEGER,Added_at TEXT,Added_by INTEGER,Updated_at TEXT,Updated_by INTEGER);
"""


class Database:
    def __init__(self):
        self.path = Path(os.getenv("WOR_DB_PATH", DEFAULT_PATH))

    def connect(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.path)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    @contextmanager
    def cursor(self):
        connection = self.connect()
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
            connection.close()

    def initialize(self):
        connection = self.connect()
        try:
            connection.executescript(SCHEMA)
            seeded = connection.execute(
                "SELECT 1 FROM app_metadata WHERE key='seed_version' AND value=?",
                (SEED_VERSION,),
            ).fetchone()
            if seeded:
                return

            seed = self._load_legacy_seed()
            connection.execute("BEGIN IMMEDIATE")
            self._insert_seed(connection, seed)
            connection.execute(
                "INSERT OR REPLACE INTO app_metadata(key,value) VALUES('seed_version',?)",
                (SEED_VERSION,),
            )
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def _load_legacy_seed(self):
        if not SEED_PATH.exists():
            raise FileNotFoundError("Missing database seed file: " + str(SEED_PATH))
        legacy = sqlite3.connect(":memory:")
        try:
            legacy.executescript(LEGACY_SCHEMA)
            legacy.execute("INSERT INTO users VALUES(1,'Admin','admin','/media/users/11-09-2021%2018%2500%20PM-Admin.png','admin@gmail.com','81dc9bdb52d04dc20036dbd8313ed055',1)")
            legacy.execute("INSERT INTO roles VALUES(1,'Admin',?,1,'2021-08-28',1,'2021-08-28',1)", (ADMIN_ACCESS,))
            legacy.execute("INSERT INTO users_log VALUES(1,'admin',1,'2021-08-31',1,'2021-09-11',1)")
            legacy.executescript(SEED_PATH.read_text(encoding="utf-8-sig"))
            return {
                "roles": legacy.execute("SELECT * FROM roles ORDER BY ID").fetchall(),
                "users": legacy.execute("SELECT u.ID,u.Name,u.User_name,u.Img_path,u.Email,u.Pswd,u.Status,l.Role,l.Added_at,l.Added_by,l.Updated_at,l.Updated_by FROM users u JOIN users_log l ON l.ID=u.ID ORDER BY u.ID").fetchall(),
                "campaigns": legacy.execute("SELECT * FROM campaign ORDER BY ID").fetchall(),
                "associates": legacy.execute("SELECT * FROM associates_info ORDER BY ID").fetchall(),
            }
        finally:
            legacy.close()

    @staticmethod
    def _insert_seed(connection, seed):
        connection.executemany("INSERT INTO roles(id,name,access_level,status,added_at,added_by,updated_at,updated_by) VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET access_level=CASE WHEN instr(roles.access_level, char(92)) > 0 THEN excluded.access_level ELSE roles.access_level END", seed["roles"])
        connection.executemany("INSERT INTO users(id,name,user_name,img_path,email,pswd,status,role_id,added_at,added_by,updated_at,updated_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET img_path=CASE WHEN users.img_path IS NULL OR trim(users.img_path)='' OR lower(users.img_path) LIKE '%/media/%' THEN excluded.img_path ELSE users.img_path END", seed["users"])
        connection.executemany("INSERT OR IGNORE INTO campaigns(id,name,status,added_at,added_by,updated_at,updated_by) VALUES(?,?,?,?,?,?,?)", seed["campaigns"])
        connection.executemany("INSERT INTO associates(id,name,designation,description,moti_quote,img_path,campaign_id,status,added_at,added_by,updated_at,updated_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET designation=CASE WHEN associates.designation='Not Know' THEN excluded.designation ELSE associates.designation END,description=CASE WHEN associates.description='Not Know' THEN excluded.description ELSE associates.description END,moti_quote=excluded.moti_quote,img_path=CASE WHEN lower(associates.img_path) LIKE '%/media/%' THEN excluded.img_path ELSE associates.img_path END", seed["associates"])


def as_status(value):
    return 1 if str(value).strip().lower() in {"1", "true", "yes", "on"} else 0


database = Database()
