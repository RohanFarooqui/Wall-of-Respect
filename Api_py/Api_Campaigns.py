##=> Imports

#=> Lib Import
from flask import request
from flask import Flask ,url_for,request,jsonify
from flask import Response
import hashlib

#=> File Import
from Database_py.Tbl_Campaigns import *

#=> Class autheticate role and provide its details
class Campaign:
    def __init__(self,db_credentials):
        self.DB_Con = db_credentials

    #-> Add Campaign
    def Add_Campaign(self):
        #--> Get Data from Request
        #-> Campaign  name
        Campaign_Name    = request.args.get('Camp_name')  
        #-> Added by
        Added_by         = request.args.get('Added_by')
        #=> Add data to DB
        Result = self.DB_Con.add_campaign(Campaign_Name,Added_by)
        if(Result == True):
            Msg = {"Message": "Added Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> View all Campaigns
    def View_Campaign(self):
        Result = list((self.DB_Con.view_campaign()))
        
        Campaigns_List  = []

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
            Campaigns_List.append(temp)

        return jsonify(Campaigns_List),200

    #-> Update Campaign info
    def Update_Campaign(self):
        #--> Get Data from Request
        #-> Campaign  name
        Campaign_Name  = request.args.get('Camp_name')
        #-> Status
        Status         = request.args.get('Status')
        #-> Updated by
        Updated_by     = request.args.get('Updated_by')
        #-> Campaign id
        Camp_id        = request.args.get('Camp_Id')
        #-> Update Campaign info
        Result = self.DB_Con.update_campaign(Campaign_Name,Status,Updated_by,Camp_id)
        if(Result == True):
            Msg = {"Message": "Updated Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> Get Total Campaign
    def Total_Campaign(self):
        Result = list((self.DB_Con.view_campaign()))
        
        Campaigns_List  = []

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
            Campaigns_List.append(temp)

        return str(len(Campaigns_List))