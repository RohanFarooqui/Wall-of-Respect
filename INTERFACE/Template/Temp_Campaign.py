##=> Imports

#=> Lib Import
from django.http.response      import HttpResponse,HttpResponsePermanentRedirect, HttpResponseRedirect 
from django.core.files.storage import FileSystemStorage
from django.shortcuts          import redirect, render
from django.views              import View  
from django.contrib            import messages
import os

#=> File Import
from INTERFACE.Api.Api_get_data              import * 
from INTERFACE.Api.Api_add_update            import * 
from INTERFACE.Other.Other_Get_Date_and_Time import * 
from INTERFACE.Logs.Other_Save_User_Logs     import *

class Campaign(View):
        def __init__(self,request):
                self.request = request
        
        def Campaign_Page(self):
            session_check = Session(self.request).Verify_Session()
            if(session_check):
                if(Session(self.request).Verify_Page_access('camp_page')):   
                    if(self.request.method == 'POST'):
                        type = self.request.POST['type']

                        if(type == "Add_Campaign"):
                            
                            resp = self.Campaign_Add()
        
                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details']))) 

                            return True

                        elif(type == "Update_Campaign"):

                            resp =self.Campaign_Update()

                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details']))) 

                            return True
                        else:

                            messages.error(self.request,"Unexpected Error .. !!")

                            return False

                        '''Check_Form_Request = self.request.POST.get('camp_id', False) 
                        if(Check_Form_Request == False):
                            resp = self.Campaign_Add()
        
                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details']))) 

                            return True

                        else:
                            resp =self.Campaign_Update()

                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details']))) 

                            return True'''
                    else:
                        return False
                else:
                    return "Page Access Not Allowed"
            else:
                return "Session Fail"

        #=> Campaign Add
        def Campaign_Add(self):
            #-> Campaign Name
            camp_name = self.request.POST['camp_name']
            #-> Added by
            added_by  = Session(self.request).Get_Id()

            #-> Creating Log
            Operation = "Added Campaign |-> Name :"+str(camp_name)
            self.Write_log_message("Add", Operation)
            
            #-> Send Data to API
            resp = form_add_campaign(camp_name,added_by)

            return resp

        #=> Campaign Update
        def Campaign_Update(self):
            #-> Campaign ID
            camp_id     = self.request.POST['camp_id']
            #-> Campaign Name 
            camp_name   = self.request.POST['camp_name']
            #-> Campaign Status
            camp_status = self.request.POST['camp_status']
            #-> Campaign Updated by
            updated_by  = Session(self.request).Get_Id()
            
            #-> Creating Log
            Operation = "Update Campaign |-> ID : "+str(camp_id)+" | Name : "+str(camp_name)+" | Status : "+str(camp_status)
            self.Write_log_message("Update", Operation)          
            
            
            #-> Send Data to API
            resp = form_update_campaign(camp_id,camp_name,camp_status,updated_by)

            return resp

        #-> Write Log to csv
        def Write_log_message(self,msg):
            try:
                Save_User_Logs_History().Write_message(msg)
            except:
                pass

        #-> Write Log to csv
        def Write_log_message(self,type,Operation):
            ID        = str(Session(self.request).Get_Id())
            User_Name = Session(self.request).Get_Name()
            Time      = get_date()
            Date      = get_time()

            #-> Add to List
            Log_Data_List =[]
            Log_Data_List.append(ID)
            Log_Data_List.append(User_Name)
            Log_Data_List.append(Operation)
            Log_Data_List.append(Time)
            Log_Data_List.append(Date)

            try:
                if(type == "Add"):
                        Save_User_Logs_History().Write_message(Log_Data_List)
                elif(type == "Update"):
                    Save_User_Logs_History().Write_message(Log_Data_List)
            except:
                pass