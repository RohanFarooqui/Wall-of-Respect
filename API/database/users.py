import sqlite3
from .connection import as_status, database

class table_users:
    def __init__(self, *args): self.database = database
    def add_user(self,name,U_name,Img_Path,Email,Pswd,Role,Added_by):
        try:
            with self.database.cursor() as c: c.execute("INSERT INTO users(name,user_name,img_path,email,pswd,role_id,status,added_by,updated_by) VALUES(?,?,?,?,?,?,1,?,?)",(name,U_name,Img_Path,Email,Pswd,Role,Added_by,Added_by))
            return True
        except sqlite3.Error as e: return str(e)
    def view_user(self):
        try:
            with self.database.cursor() as c: return c.execute("SELECT u.id,u.name,u.user_name,u.img_path,u.email,u.pswd,u.status,r.name,u.added_at,COALESCE(a.user_name,'-'),u.updated_at,COALESCE(b.user_name,'-') FROM users u JOIN roles r ON r.id=u.role_id LEFT JOIN users a ON a.id=u.added_by LEFT JOIN users b ON b.id=u.updated_by ORDER BY u.id").fetchall()
        except sqlite3.Error as e: return str(e)
    def update_user_info(self,name,U_name,Img_Path,Email,Role,Status,Updated_by,User_id):
        try:
            with self.database.cursor() as c: c.execute("UPDATE users SET name=?,user_name=?,img_path=?,email=?,role_id=?,status=?,updated_at=CURRENT_DATE,updated_by=? WHERE id=?",(name,U_name,Img_Path,Email,Role,as_status(Status),Updated_by,User_id))
            return True
        except sqlite3.Error as e: return str(e)
    def update_user_pswd(self,Pswd,Updated_by,User_id):
        try:
            with self.database.cursor() as c: c.execute("UPDATE users SET pswd=?,updated_at=CURRENT_DATE,updated_by=? WHERE id=?",(Pswd,Updated_by,User_id))
            return True
        except sqlite3.Error as e: return str(e)
    def verify_user(self,user_name,pswd):
        try:
            with self.database.cursor() as c: return c.execute("SELECT 1 FROM users WHERE user_name=? AND pswd=? AND status=1",(user_name,pswd)).fetchone() is not None
        except sqlite3.Error: return False
    def get_user_details(self,user_name,pswd):
        try:
            with self.database.cursor() as c: return c.execute("SELECT u.id,u.name,u.user_name,u.img_path,u.email,r.access_level FROM users u JOIN roles r ON r.id=u.role_id WHERE u.user_name=? AND u.pswd=? AND u.status=1",(user_name,pswd)).fetchall()
        except sqlite3.Error as e: return str(e)
