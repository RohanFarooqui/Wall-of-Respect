# ==> Imports 

# => Flask Lib
import re
from flask                 import Flask ,url_for,request,jsonify

# => Other Lib
from   datetime import datetime
import emoji

# => File Imports

# ==> Database Py Files
from Database_py.Tbl_Users import *
from Database_py.Tbl_Roles import *
from Database_py.Tbl_Campaign import *

# ==> Api Py Files
from Api_py.Api_Users import *
from Api_py.Api_Roles import *
from Api_py.Api_Campaign import *



# => Database Connection 
try:
    DB_Con_1 =  table_users('sql6.freemysqlhosting.net','sql6437945','isxEqZIuys','sql6437945')      
    DB_Con_2 =  table_roles('sql6.freemysqlhosting.net','sql6437945','isxEqZIuys','sql6437945')      
    #DB_Con_3 =  table_associates('sql6.freemysqlhosting.net','sql6437945','isxEqZIuys','sql6437945') 
    DB_Con_4 =  table_Campaign('sql6.freemysqlhosting.net','sql6437945','isxEqZIuys','sql6437945')
    Database_Status = "Perfect !!"
except:
    Database_Status = "Connection Error !!"

# => Flask 
app = Flask(__name__)

#=> Main Class
class main:
    def __init__(self):
        self.app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    ## ==> Default Route
    @app.route("/",methods=['GET'])
    def main():
        Msg = { "1.Name ": "Wall of Respect",
                "2.Api Version": "1.0",
                "3.Developed by" : "M.ROHAN FAROOQUI©",
                "4.API Status" : "Running "+emoji.emojize(":grinning_face_with_big_eyes:"),
                "5.Database Status " :  Database_Status }
        return jsonify(Msg),200

    ########################### ==> User API <== ###########################
    
    ######## => Add , View & Update  <= ########
    @app.route("/v1/user",methods=['GET','POST','PUT'])
    def User():
        if(request.method == 'POST' and 'Added_by' in request.args):
            Result_1 = User(DB_Con_1).Add_User()
            return Result_1
        elif(request.method == 'POST' and 'Name' in request.args):  ### For Info Update
            Result_2 = User(DB_Con_1).Update_User_info()
            return Result_2
        elif(request.method == 'POST' and 'Pswd' in request.args):  ### For Password Update
            Result_3 = User(DB_Con_1).Update_User_Pswd()
            return Result_3            
        elif(request.method == 'GET'):
            Result_4 = User(DB_Con_1).View_User()
            return Result_4

    ########################### ==> Role API      <== ###########################

    ######## => Add , View & Update  <= ########
    @app.route("/v1/role",methods=['GET','POST'])
    def Role():
        if(request.method == 'POST' and 'Added_by' in request.args):
            Result_1 = Role(DB_Con_2).Add_Role()
            return Result_1
        elif(request.method == 'POST' and 'Updated_by' in request.args):
            Result_2 = Role(DB_Con_2).Update_Role()
            return Result_2
        elif(request.method == 'GET'):
            Result_3 = Role(DB_Con_2).View_Role()
            return Result_3

    ########################### ==> Campaign API  <== ###########################

    ######## => Add , View & Update  <= ########
    @app.route("/v1/campaign",methods=['GET','POST'])
    def Campaign():
        if(request.method == 'POST' and 'Added_by' in request.args):
            Result_1 = Campaign(DB_Con_4).Add_Campaign()
            return Result_1
        elif(request.method == 'POST' and 'Updated_by' in request.args):
            Result_2 = Campaign(DB_Con_4).Update_Campaign()
            return Result_2
        elif(request.method == 'GET'):
            Result_3 = Campaign(DB_Con_4).View_Campaign()
            return Result_3

if __name__ == '__main__':
    app.run(debug=True)  ## For Debug
    #app.run()