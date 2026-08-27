##=> Imports

#=> Lib Import
from flask import request
from flask import Flask ,url_for,request,jsonify
from flask import Response
import hashlib

#=> File Import

#=> Class autheticate role and provide its details
class Role:
    def __init__(self,db_credentials):
        self.DB_Con = db_credentials

    #-> Add Role
    def Add_Role(self):
        #--> Get Data from Request
        #-> Role name
        Role_name    = request.args.get('Role_name')
        #-> Role access
        Access_level = request.args.get('Role_access')
        #-> Added by
        Added_by     = request.args.get('Added_by')
        #=> Add data to DB
        Result = self.DB_Con.add_role(Role_name,Access_level,Added_by)
        if(Result == True):
            Msg = {"Message": "Added Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> View all Role
    def View_Role(self):
        Result = list((self.DB_Con.view_role()))
        
        Role_list = []

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
            Role_list.append(temp)

        return jsonify(Role_list),200

    #-> Update role info
    def Update_Role(self):
        #--> Get Data from Request
        #-> Role name
        Role_name    = request.args.get('Role_name')
        #-> Role access
        Access_level = request.args.get('Role_access')
        #-> Status
        Status      = request.args.get('Status')
        #-> Updated by
        Updated_by  = request.args.get('Updated_by')
        #-> Roll id
        Roll_id     = request.args.get('Roll_id')
        #-> Update role info
        Result = self.DB_Con.update_role(Role_name,Access_level,Status,Updated_by,Roll_id)
        if(Result == True):
            Msg = {"Message": "Updated Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> Get Total Role
    def Total_Role(self):
        Result = list((self.DB_Con.view_role()))
        
        Role_list = []

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
            Role_list.append(temp)
        
        return str(len(Role_list))
