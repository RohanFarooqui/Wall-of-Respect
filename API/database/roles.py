import sqlite3
from .connection import as_status, database
class table_roles:
    def __init__(self,*args): self.database=database
    def add_role(self,name,access,added):
        try:
            with self.database.cursor() as c: c.execute("INSERT INTO roles(name,access_level,status,added_by,updated_by) VALUES(?,?,1,?,?)",(name,access,added,added))
            return True
        except sqlite3.Error as e: return str(e)
    def view_role(self):
        try:
            with self.database.cursor() as c: return c.execute("SELECT r.id,r.name,r.access_level,r.status,r.added_at,COALESCE(a.user_name,'-'),r.updated_at,COALESCE(b.user_name,'-') FROM roles r LEFT JOIN users a ON a.id=r.added_by LEFT JOIN users b ON b.id=r.updated_by ORDER BY r.id").fetchall()
        except sqlite3.Error as e: return str(e)
    def update_role(self,name,access,status,updated,role_id):
        try:
            value=as_status(status)
            with self.database.cursor() as c:
                c.execute("UPDATE roles SET name=?,access_level=?,status=?,updated_at=CURRENT_DATE,updated_by=? WHERE id=?",(name,access,value,updated,role_id)); c.execute("UPDATE users SET status=? WHERE role_id=?",(value,role_id))
            return True
        except sqlite3.Error as e: return str(e)
