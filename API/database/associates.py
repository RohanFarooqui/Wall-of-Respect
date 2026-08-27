import sqlite3
from .connection import as_status, database
class table_associates:
    def __init__(self,*args): self.database=database
    def add_associate(self,name,desig,desc,quote,img,camp,added):
        try:
            with self.database.cursor() as c: c.execute("INSERT INTO associates(name,designation,description,moti_quote,img_path,campaign_id,status,added_by,updated_by) VALUES(?,?,?,?,?,?,1,?,?)",(name,desig,desc,quote,img,camp,added,added))
            return True
        except sqlite3.Error as e: return str(e)
    def view_associates(self):
        try:
            with self.database.cursor() as c: return c.execute("SELECT s.id,s.name,s.designation,s.description,s.moti_quote,s.img_path,x.name,s.status,s.added_at,COALESCE(a.user_name,'-'),s.updated_at,COALESCE(b.user_name,'-') FROM associates s JOIN campaigns x ON x.id=s.campaign_id LEFT JOIN users a ON a.id=s.added_by LEFT JOIN users b ON b.id=s.updated_by ORDER BY s.id").fetchall()
        except sqlite3.Error as e: return str(e)
    def update_associates(self,name,desig,desc,quote,img,camp,status,updated,assc_id):
        try:
            with self.database.cursor() as c: c.execute("UPDATE associates SET name=?,designation=?,description=?,moti_quote=?,img_path=?,campaign_id=?,status=?,updated_at=CURRENT_DATE,updated_by=? WHERE id=?",(name,desig,desc,quote,img,camp,as_status(status),updated,assc_id))
            return True
        except sqlite3.Error as e: return str(e)
