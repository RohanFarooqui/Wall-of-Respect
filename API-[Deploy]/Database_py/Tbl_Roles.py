# => My SQl Lib
import pymysql as mysql


# => Class : DB table Users
class table_roles:
    def __init__(self,host,user_name,pswd,db):
        self.db = mysql.connect(host=host, user=user_name, passwd=pswd, db=db,autocommit=True)
        self.cur = self.db.cursor()

    # => Add New Role
    def add_role(self,role_name,access_level,added_by):
        self.db.ping()
        try:
            part_1  = "CALL `Add_Role` (%s,%s,%s)"
            part_2  = (role_name,access_level,added_by)
            self.cur.execute(part_1,part_2)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])
    
    # => View Roles
    def view_role(self):
        self.db.ping()
        try:
            part_1 = "call list_Roll()"
            self.cur.execute(part_1)
            User_Record = self.cur.fetchall()
            return User_Record
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

    # => Update Roles
    def update_role(self,roll_name,access_level,status,updated_by,roll_id):
        self.db.ping()
        try:
            query = "CALL `Update_Role`(%s,%s,%s,%s,%s)"
            param = (roll_name,access_level,status,updated_by,roll_id)
            print(param)
            self.cur.execute(query,param)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

