import sqlite3
from .connection import as_status, database
class table_Campaign:
    def __init__(self,*args): self.database=database
    def add_campaign(self,name,added):
        try:
            with self.database.cursor() as c: c.execute("INSERT INTO campaigns(name,status,added_by,updated_by) VALUES(?,1,?,?)",(name,added,added))
            return True
        except sqlite3.Error as e: return str(e)
    def view_campaign(self):
        try:
            with self.database.cursor() as c: return c.execute("SELECT x.id,x.name,x.status,x.added_at,COALESCE(a.user_name,'-'),x.updated_at,COALESCE(b.user_name,'-') FROM campaigns x LEFT JOIN users a ON a.id=x.added_by LEFT JOIN users b ON b.id=x.updated_by ORDER BY x.id").fetchall()
        except sqlite3.Error as e: return str(e)
    def update_campaign(self,name,status,updated,camp_id):
        try:
            value=as_status(status)
            with self.database.cursor() as c:
                c.execute("UPDATE campaigns SET name=?,status=?,updated_at=CURRENT_DATE,updated_by=? WHERE id=?",(name,value,updated,camp_id)); c.execute("UPDATE associates SET status=? WHERE campaign_id=?",(value,camp_id))
            return True
        except sqlite3.Error as e: return str(e)
