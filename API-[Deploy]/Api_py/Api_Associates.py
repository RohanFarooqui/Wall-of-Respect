##=> Imports

#=> Lib Import
from flask import request
from flask import Flask ,url_for,request,jsonify
from flask import Response
import hashlib
from operator import itemgetter

#=> File Import
from Database_py.Tbl_Associates import *

#=> Class autheticate role and provide its details
class Associate:
    def __init__(self,db_credentials):
        self.DB_Con = db_credentials

    #-> Add Associate
    def Add_Associate(self):
        #--> Get Data from Request
        #-> Associate  name
        Assc_Name        = request.args.get('Assc_name')
        #-> Designation
        Designation      = request.args.get('Desig')
        #-> Description
        Description      = request.args.get('Descrip')
        #-> Motivational Quote
        Moti_quote       = request.args.get('Quote')
        #-> Image Parh
        Img_path         = request.args.get('Img_path')
        #-> Campaign id
        Campaign_id      = request.args.get('Camp')
        #-> Added by
        Added_by         = request.args.get('Added_by')
        #=> Add data to DB
        Result = self.DB_Con.add_associate(Assc_Name,Designation,Description,Moti_quote,Img_path,Campaign_id,Added_by)
        if(Result == True):
            Msg = {"Message": "Added Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> View all Associates
    def View_Associate(self):
        Result = list((self.DB_Con.view_associates()))
        
        Associates_List  = []

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
            Associates_List.append(temp)
            
        return jsonify(Associates_List),200

    #-> Update Associate info
    def Update_Associate(self):
        #--> Get Data from Request
        #-> Associate  name
        Assc_Name        = request.args.get('Assc_name')
        #-> Designation
        Designation      = request.args.get('Desig')
        #-> Description
        Description      = request.args.get('Descrip')
        #-> Motivational Quote
        Moti_quote       = request.args.get('Quote')
        #-> Image Parh
        Img_path         = request.args.get('Img_path')
        #-> Campaign id
        Campaign_id      = request.args.get('Camp_id')
        #-> Status
        Status           = request.args.get('Status')
        #-> Updated by
        Updated_by       = request.args.get('Updated_by')
        #-> Associate id
        Assc_id          = request.args.get('Assc_id')
        #-> Update associate info
        Result = self.DB_Con.update_associates(Assc_Name,Designation,Description,Moti_quote,Img_path,Campaign_id,Status,Updated_by,Assc_id)
        if(Result == True):
            Msg = {"Message": "Updated Successfully","Response":200}
            return jsonify(Msg),200
        else:
            Result = Result.split('for')[0]
            Msg = {"Message": "Unsuccessfull","Details": str(Result),"Response":401}
            return jsonify(Msg),401

    #-> Get Total Associate
    def Total_Associate(self):
        Result = list((self.DB_Con.view_associates()))
        
        Associates_List  = []

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
            Associates_List.append(temp)
        
        return str(len(Associates_List))