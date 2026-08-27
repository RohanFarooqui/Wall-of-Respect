# ==> Imports 

# => Flask Lib
import re
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory

# => Other Lib
from   datetime import datetime
import emoji

# => File Imports

# ==> Database Py Files
from database.users import table_users
from database.roles import table_roles
from database.associates import table_associates
from database.campaigns import table_Campaign

# ==> Api Py Files
from api.login import Login
from api.users import User
from api.roles import Role
from api.associates import Associate
from api.campaigns import Campaign
from api.media import Media
from database.connection import database


# => Database Connection 
try:
    database.initialize()
    DB_Con_1 = table_users()
    DB_Con_2 = table_roles()
    DB_Con_3 = table_associates()
    DB_Con_4 = table_Campaign()
    Database_Status = "Perfect !!"
except Exception as error:
    Database_Status = "Connection Error: " + str(error)

# => Flask 
app = Flask(__name__)
MEDIA_ROOT = Path(__file__).resolve().parent / "media"

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

    @app.route("/media/<path:filename>", methods=['GET'])
    def media(filename):
        return send_from_directory(MEDIA_ROOT, filename)

    @app.route("/v1/media", methods=['POST'])
    def upload_media():
        return Media.upload()

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

    ########################### ==> Associate API <== ###########################

    ######## => Add , View & Update  <= ########
    @app.route("/v1/associate",methods=['GET','POST'])
    def Associate():
        if(request.method == 'POST' and 'Added_by' in request.args):
            Result_1 = Associate(DB_Con_3).Add_Associate()
            return Result_1
        elif(request.method == 'POST' and 'Updated_by' in request.args):
            Result_2 = Associate(DB_Con_3).Update_Associate()
            return Result_2
        elif(request.method == 'GET'):
            Result_3 = Associate(DB_Con_3).View_Associate()
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

    ########################### ==> Other API's   <== ############################

    ######## => User Login API  <= ########
    @app.route("/v1/login",methods=['POST'])
    def login_user():
        verify_user = Login(DB_Con_1).Login_User()
        return verify_user
    
    ######## => Total User's Api <= ########
    @app.route("/v1/total-user",methods=['GET'])
    def Total_User():
            Result_1 = User(DB_Con_1).Total_User()
            return Result_1
    
    ######## => Total Role's Api <= ########
    @app.route("/v1/total-role",methods=['GET'])
    def Total_Role():
            Result_1 = Role(DB_Con_2).Total_Role()
            return Result_1
    
    ######## => Total Associate's Api <= ########
    @app.route("/v1/total-associate",methods=['GET'])
    def Total_Associate():
            Result_1 = Associate(DB_Con_3).Total_Associate()
            return Result_1

    ######## => Total Campaign Api <= ########
    @app.route("/v1/total-campaign",methods=['GET'])
    def Total_Campaign():
            Result_1 = Campaign(DB_Con_4).Total_Campaign()
            return Result_1

#=> Main 
if __name__ == '__main__':
    app.run()