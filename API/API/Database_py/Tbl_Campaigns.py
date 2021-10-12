# => My SQl Lib
import pymysql as mysql


# => Class : DB table Campaign
class table_Campaign:
    def __init__(self,host,user_name,pswd,db):
        self.db = mysql.connect(host=host, user=user_name, passwd=pswd, db=db,autocommit=True)
        self.cur = self.db.cursor()

    # => Add Campaign
    def add_campaign(self,camp_name,added_by):
        self.db.ping()
        try:
            part_1 = "call Add_Campaign(%s,%s)"
            part_2 = (camp_name,added_by)
            self.cur.execute(part_1,part_2)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])
                
    # => View Campaign
    def view_campaign(self):
        self.db.ping()
        try:
            part_1 = "call list_Campaign()"
            self.cur.execute(part_1)
            User_Record = self.cur.fetchall()
            return User_Record
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

    # => Update Roles
    def update_campaign(self,campaign_name,status,updated_by,campaign_id):
        self.db.ping()
        try:
            query = "CALL `Update_Campaign`(%s,%s,%s,%s)"
            param = (campaign_name,status,updated_by,campaign_id)
            self.cur.execute(query,param)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

