##=> Imports

#=> Lib Import
from django.http.response      import HttpResponse,HttpResponsePermanentRedirect, HttpResponseRedirect 
from django.core.files.storage import FileSystemStorage
from django.shortcuts          import redirect, render
from django.views              import View  
from django.contrib            import messages
import os

#=> File Import
from Dashboard.Api.Api_get_data              import * 
from Dashboard.Api.Api_add_update            import * 
from Dashboard.Other.Other_Get_Date_and_Time import * 
from Dashboard.Logs.Other_Save_User_Logs     import *

 

class User(View):
        def __init__(self,request):
            self.request = request

        #=> User Page
        def User_Page(self):
            session_check = Session(self.request).Verify_Session()
            if(session_check):
                if(Session(self.request).Verify_Page_access('user_page')):
                    if(self.request.method == 'POST'):
                        type = self.request.POST['type']

                        if(type == "add_user"):
                            resp = self.User_Add()

                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details'])))     
                                                             
                            return True

                        elif(type == "update_user_info"):
                            resp = self.User_Update_info()
                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details']))) 

                            return True

                        elif(type == "update_user_pswd" ):
                            resp = self.User_Update_pswd()
                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details']))) 
                            
                            return True

                        else:
                            messages.error(self.request,"Unexpected Error .. !!")
                            return False

                    else:
                        return False
                else:
                    return "Page Access Not Allowed"
            else:
                return "Session Fail"

        #=> User Add
        def User_Add(self):
            #-> Name
            name = self.request.POST['name']
            #-> User Name
            u_name = self.request.POST['u_name']
            #-> Email
            email = self.request.POST['email']
            #-> Password
            pswd  = self.request.POST['pswd']
            #-> Role
            role  = self.request.POST['role']
            #-> Image
            img_name = self.request.FILES['img']
            fss = FileSystemStorage()
            file_ext    = str(img_name).split('.')[-1]
            new_image_name = str(get_date_time())+"-"+name+"."+file_ext
            file = fss.save(new_image_name, img_name )
            image_url = fss.url(file)
            #-> Added by
            added_by = Session(self.request).Get_Id()

            #-> Creating Log
            Operation = "Addded User |-> Name :"+str(name)+" | User Name :"+str(u_name)+" | Email :"+str(email)+" | Role :"+str(role)
            self.Write_log_message("Add", Operation)

            #-> Send Data to API
            resp = form_add_user(name,u_name,image_url,email,pswd,role,added_by)     

            return resp

        #=> User Update Info
        def User_Update_info(self):
            #-> User ID
            user_id = self.request.POST['user_id']
            #-> Name
            name = self.request.POST['name']
            #-> User Name
            u_name = self.request.POST['u_name']
            #-> Email
            email = self.request.POST['email']
            #-> Role
            role  = self.request.POST['role']
            #-> Image
            new_upload = self.request.FILES.get('img', False)
            if(new_upload != False):
                img_name = self.request.FILES['img']
                fss = FileSystemStorage()
                file_ext    = str(img_name).split('.')[-1]
                new_image_name = str(get_date_time())+"-"+name+"."+file_ext
                file = fss.save(new_image_name, img_name )
                image_url = fss.url(file)

                previous_img = self.request.POST['img_1']
                previous_img_url = os.getcwd()+"\\"+previous_img.replace("/","\\")
                try:
                    os.remove(previous_img_url)
                except:
                    pass
            else:
                image_url= self.request.POST['img_1']
            #-> Status
            status = self.request.POST['status']
            #-> Updated by
            updated_by = Session(self.request).Get_Id()

            #-> Creating Log
            Operation = "Updated User Info |-> ID : "+str(user_id)+"Name : "+str(name)+" | User_Name : "+str(u_name)+" | Email : "+str(email)+" | Role : "+str(role)+" | Status : "+str(status)
            self.Write_log_message("Update", Operation)

            #-> Send Data to API
            resp = form_update_user_info(name,u_name,image_url,email,role,status,updated_by,user_id)

            #-> Delete Session as User Password Update
            Session.Delete_Session(self, user_id)

            return resp

        #=> User Update Pswd
        def User_Update_pswd(self):
            #-> User ID
            user_id = self.request.POST['user_id']
            #-> Password
            pswd    = self.request.POST['pswd']
            #-> Updated by
            updated_by = Session(self.request).Get_Id()
            #-> Creating Log
            Operation = "Updated User Pswd |-> ID : "+str(user_id)
            self.Write_log_message("Update Password", Operation)

            #-> Send Data to API
            resp = form_update_user_pswd(pswd, updated_by, user_id)

            #-> Delete Session as User Password Update
            Session.Delete_Session(self, user_id)

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