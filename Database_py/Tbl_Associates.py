# => My SQl Lib
import pymysql as mysql


# => Class : DB table Users
class table_associates:
    def __init__(self,host,user_name,pswd,db):
        self.db = mysql.connect(host=host, user=user_name, passwd=pswd, db=db,autocommit=True)
        self.cur = self.db.cursor()

    # => Add New Associate
    def add_associate(self,name,Desig,Descrip,Moti_Quote,Img_Path,Campaign_id,Added_by):
        self.db.ping()
        try:
            part_1  = "CALL `Add_Associate` (%s,%s,%s,%s,%s,%s,%s)"
            part_2  = (name,Desig,Descrip,Moti_Quote,Img_Path,Campaign_id,Added_by)
            self.cur.execute(part_1,part_2)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])
    
    # => View Associate's
    def view_associates(self):
        self.db.ping()
        try:
            part_1 = "call list_Associates()"
            self.cur.execute(part_1)
            User_Record = self.cur.fetchall()
            return User_Record
        except mysql.Error as e:
            self.db.rollback()
            return str(e.args[1])

    # => Update Associate
    def update_associates(self,name,desig,Descrip,Moti_Quote,Img_path,Campaign_id,Status,Updated_by,assc_id):
        self.db.ping()
        try:
            query = "CALL `Update_Associate`(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = (name,desig,Descrip,Moti_Quote,Img_path,Campaign_id,Status,Updated_by,assc_id)
            print(param)
            self.cur.execute(query,param)
            self.db.commit()
            return True
        except mysql.Error as e:
            self.db.rollback()
            print(e)
            return str(e.args[1])

