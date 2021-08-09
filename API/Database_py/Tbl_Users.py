# => My SQl Lib
import pymysql as mysql


# => Class : DB table Users
class table_users:
    def __init__(self,host,user_name,pswd,db):
        self.db = mysql.connect(host=host, user=user_name, passwd=pswd, db=db,autocommit=True)
        self.cur = self.db.cursor()

    # => Add New User
    def add_user(self,name,U_name,Img_Path,Email,Pswd,Role,Added_by):
        self.db.ping()
        try:
            part_1  = "CALL `Add_User` (%s,%s,%s,%s,%s,%s,%s)"
            part_2  = (name,U_name,Img_Path,Email,Pswd,Role,Added_by)
            self.cur.execute(part_1,part_2)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])
   
    # => View Users
    def view_user(self):
        self.db.ping()
        try:
            part_1 = "call list_User()"
            self.cur.execute(part_1)
            User_Record = self.cur.fetchall()
            return User_Record
        except mysql.Error  as e:
            self.db.rollback()
            return str(e.args[1]) 

    # => Update User Info
    def update_user_info(self,name,U_name,Img_Path,Email,Role,Status,Updated_by,User_id):
        self.db.ping()
        try:
            query = "CALL `Update_User_Info`(%s,%s,%s,%s,%s,%s,%s,%s)"
            param = (name,U_name,Img_Path,Email,Role,Status,Updated_by,User_id)
            self.cur.execute(query,param)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

    # => Update User Password
    def update_user_pswd(self,Pswd,Updated_by,User_id):
        self.db.ping()
        try:
            query = "CALL `Update_User_Password`(%s,%s,%s)"
            param = (Pswd,Updated_by,User_id)
            self.cur.execute(query,param)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])
    
    # => Login Users
    def verify_user(self,user_name,pswd):
        self.db.ping()
        try:
            query = " SELECT `Verify_login`(%s,%s);"
            param = (user_name,pswd)
            self.cur.execute(query,param)
            Check = self.cur.fetchone()        
            if(Check[0] == 1):
                return True
            else:
                return False
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

    # => Get User Details After Login
    def get_user_details(self,user_name,pswd):
        self.db.ping()
        try:
            query = " CALL `Get_User_Details`(%s,%s);"
            param = (user_name,pswd)
            self.cur.execute(query,param)
            User_Details = self.cur.fetchall()
            return User_Details
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

