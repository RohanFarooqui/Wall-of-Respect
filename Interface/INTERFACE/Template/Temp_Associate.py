##=> Imports

#=> Lib Import
from django.http.response      import HttpResponse,HttpResponsePermanentRedirect, HttpResponseRedirect 
from django.shortcuts          import redirect, render
from django.views              import View  
from django.contrib            import messages

#=> File Import
from INTERFACE.Api.Api_get_data              import * 
from INTERFACE.Api.Api_add_update            import * 
from INTERFACE.Other.Other_Get_Date_and_Time import * 
from INTERFACE.Logs.Other_Save_User_Logs     import *


class Associate(View):
        def __init__(self,request):
            self.request = request

        #=> Associate Page
        def Associate_Page(self):
            session_check = Session(self.request).Verify_Session()
            if(session_check):
                if(Session(self.request).Verify_Page_access('assc_page')):
                    if(self.request.method == 'POST'):
                        type = self.request.POST['type']

                        if(type == "Add_Associate"):
                            resp = self.Associate_Add() 

                            if(resp['Response'] == 200):
                                messages.success(self.request,resp['Message'])
                            elif(resp['Response']== 401):
                                messages.error(self.request,(str(resp['Message'])+" : "+str(resp['Details'])))

                            return True

                        
                        elif(type == "Update_Associate"):

                            resp = self.Associate_Update()

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

        #=> Associate Add
        def Associate_Add(self):
            #-> First Name
            name = self.request.POST['Name']
            #-> Designation
            desig = self.request.POST['desig']
            #-> Image 
            img_name = self.request.FILES['img']
            image_url = form_upload_image(img_name, 'associates')
            #-> Campaign ID
            camp   = self.request.POST['camp']
            #-> Description for Associate
            descrip= self.request.POST['descrip']
            #-> Quote for Associate
            quote  = self.request.POST['quote']
            #-> Added by
            added_by = Session(self.request).Get_Id()

            #-> Creating Log
            Operation = "Added Associate    |-> Name : "+str(name)+" | Design :"+str(desig) +" | Camp :"+str(camp)+" | Descrip :"+str(descrip)+" | Quote :"+str(quote)
            self.Write_log_message("Add", Operation)

            #-> Send Data to API & Get Response
            Resp = form_add_associate(name,image_url,camp,desig,descrip,quote,added_by) 
            
            return Resp

        #=> Associate Update
        def Associate_Update(self):
            #-> Associate ID 
            ass_id = self.request.POST['assc_id']
            #-> First Name
            name = self.request.POST['Name']
            #-> Designation
            design  = self.request.POST['desig']
            #-> Image 
            new_upload = self.request.FILES.get('img', False)
            if(new_upload != False):
                img_name = self.request.FILES['img']
                image_url = form_upload_image(img_name, 'associates')
            else:
                image_url= self.request.POST['img_1']
            #-> Campaign ID
            camp   = self.request.POST['camp']
            #-> Status 
            status = self.request.POST['status']
            #-> Description for Associate
            descrip= self.request.POST['descrip']
            #-> Quote for Associate
            quote  = self.request.POST['quote']
            #-> Updated by
            updated_by= Session(self.request).Get_Id()

            #-> Creating Log
            Operation = "Updated Asscociate | -> ID :"+str(ass_id)+"Name : "+str(name)+" | Design :"+str(design) +" | Camp :"+str(camp)+" | Status :"+str(status)+" | Descrip :"+str(descrip)+" | Quote :"+str(quote)
            self.Write_log_message("Update", Operation)

            #-> Send Data to API
            resp = form_update_associate(name,design,descrip,quote,image_url,camp,status,updated_by,ass_id)

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

                    




                
        
