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
from INTERFACE.Other.Other_Get_Role_List     import * 
from INTERFACE.Logs.Other_Save_User_Logs     import *

class Role(View):
        def __init__(self,request):
                self.request = request
        
        def Role_Page(self):
            session_check = Session(self.request).Verify_Session()
            if(session_check):
                if(Session(self.request).Verify_Page_access('role_page')):   
                    if(self.request.method == 'POST'):
                        Check_Form_Request = self.request.POST.get('roll_id', False) 
                        if(Check_Form_Request == False):
                            resp = self.Role_Add()

                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details'])))     

                            return True
                        else:

                            resp = self.Role_Update()

                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details'])))                            

                            return True
                    else:
                        return False
                else:
                    return "Page Access Not Allowed"
            else:
                return "Session Fail"

        #=> Role Add
        def Role_Add(self):
            print("Add Role")
            #-> Role Name
            role_name = self.request.POST['roll_name']
            #-> Role Access List
            user_list   = self.request.POST.getlist('user')  
            assc_list   = self.request.POST.getlist('role')  
            role_list   = self.request.POST.getlist('assc')  
            camp_list   = self.request.POST.getlist('camp')  
            role_access = get_role_list(user_list,assc_list,role_list,camp_list)
            
            #-> Added by 
            added_by =  Session(self.request).Get_Id()

            #-> Creating Log
            Operation = "Added Role |-> Name : "+str(role_name)+" | Role Access : "+str(role_access)
            self.Write_log_message("Add", Operation)
            
            #-> Send Data to API
            resp = form_add_role(role_name,role_access,added_by)

            return resp

        #=> Role Update
        def Role_Update(self):
            print("Update Role")
            #-> Role ID 
            role_id = self.request.POST['roll_id']
            #-> Role Name
            role_name = self.request.POST['roll_name']
            #-> Role Access List
            user_list = self.request.POST.getlist('user')  
            assc_list = self.request.POST.getlist('role')  
            role_list = self.request.POST.getlist('assc')  
            camp_list = self.request.POST.getlist('camp') 
            role_access = get_role_list(user_list,assc_list,role_list,camp_list)
            #-> Role Status
            role_status = self.request.POST['status']
            #-> Updated by
            updated_by = Session(self.request).Get_Id()

            #-> Creating Log
            Operation = "Updated Role |-> ID :"+str(role_id)+"Name : "+str(role_name)+" | Role Access : "+str(role_access)+" | Status :"+str(role_status)
            self.Write_log_message("Update", Operation)

            #-> Sending Data Over API
            resp = form_update_role(role_name,role_access,role_status,updated_by,role_id)

            return resp

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