##=> Imports

#=> Lib Import
from flask import request
from flask import Flask ,url_for,request,jsonify
from flask import Response
import hashlib

#=> File Import
from Database_py.Tbl_Users import *

#=> Class autheticate user and provide its details
class Login:
    def __init__(self,db_credentials):
        self.DB_Con = db_credentials

    def Login_User(self):
        #--> Get Data from Request
        #-> User Name 
        User_name = request.args.get('User_Name')
        #-> Password
        Password  = hashlib.md5(str(request.args.get('Password')).encode('utf-8')).hexdigest()  
        #-> Check if User is valid
        Result_1  = self.DB_Con.verify_user(User_name,Password)
        #-> If user is valid send his details
        if(Result_1):
            #-> Get user details
            Result_2 = self.DB_Con.get_user_details(User_name,Password)
            #-> Convert it into json
            Resp = jsonify(Result_2)
            return Resp,200 
        else:
            #-> Invalid user msg
            Msg = {"Message": "Unauthorized"}
            return jsonify(Msg),401

     