##=> Imports

#=> Lib Import
from flask import request
from flask import Flask ,url_for,request,jsonify
import hashlib

#=> File Import
from Database_py.Tbl_Users import *

#=> Class autheticate user and provide its details
class User:
    def __init__(self,db_credentials):
        self.DB_Con = db_credentials

    #-> Add User
    def Add_User(self):
        #--> Get Data from Request
        #-> Name 
        Name        = request.args.get('Name')
        #-> User Name
        User_name   = request.args.get('User_name')
        #-> Image Path
        Img_Path    = request.args.get('Img_path')
        #-> Email
        Email       = request.args.get('Email')
        #-> Password
        Pswd        = hashlib.md5(str(request.args.get('Pswd')).encode('utf-8')).hexdigest()
        #-> Role
        Role        = request.args.get('Role')
        #-> Added by
        Added_by    = request.args.get('Added_by')
        #-> Add data to DB
        Result = self.DB_Con.add_user(Name,User_name,Img_Path,Email,Pswd,Role,Added_by)
        if(Result == True):
            Msg = {"Message": "Added Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> View all User
    def View_User(self):
        Result = list((self.DB_Con.view_user()))

        User_List = []

        #-> It Convert Date to DD/MM/YYY format
        for i in Result:
            temp = []
            for j in i:
                j = str(j)
                if( "None" in j):
                    temp.append("-")
                elif("GMT" in j):
                    temp.append(str(a.split(' ')[1])+"-"+str(a.split(' ')[2])+"-"+str(a.split(' ')[3]))
                else:
                    temp.append(j)
            User_List.append(temp)
       
        return jsonify(User_List),200

    #-> Update user info
    def Update_User_info(self):
        #--> Get Data from Request
        #-> Name 
        Name        = request.args.get('Name')
        #-> User Name
        User_name   = request.args.get('User_name')
        #-> Image Path
        Img_Path    = request.args.get('Img_path')
        #-> Email
        Email       = request.args.get('Email')
        #-> Role
        Role        = request.args.get('Role')
        #-> Status
        Status      = request.args.get('Status')
        #-> Updated by
        Updated_by  = request.args.get('Updated_by')
        #-> User id
        User_id     = request.args.get('User_id')
        #-> Update user info
        Result = self.DB_Con.update_user_info(Name,User_name,Img_Path,Email,Role,Status,Updated_by,User_id)
        if(Result == True):
            Msg = {"Message": "Updated Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> Update user info
    def Update_User_Pswd(self):
        #--> Get Data from Request
        #-> Password
        Pswd        = hashlib.md5(str(request.args.get('Pswd')).encode('utf-8')).hexdigest()
        #-> Updated by
        Updated_by  = request.args.get('Updated_by')
        #-> User id
        User_id     = request.args.get('User_id')
        #-> Update user info
        Result = self.DB_Con.update_user_pswd(Pswd,Updated_by,User_id)
        if(Result == True):
            Msg = {"Message": "Password updated successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401


    #-> Get Total User
    def Total_User(self):
        Result = list((self.DB_Con.view_user()))

        User_List = []

        #-> It Convert Date to DD/MM/YYY format
        for i in Result:
            temp = []
            for j in i:
                j = str(j)
                if( "None" in j):
                    temp.append("-")
                elif("GMT" in j):
                    temp.append(str(a.split(' ')[1])+"-"+str(a.split(' ')[2])+"-"+str(a.split(' ')[3]))
                else:
                    temp.append(j)
            User_List.append(temp)
       
        return str(len(User_List))