##=> Imports

#=> Lib Import
from django.views import View

#=> File Import
from INTERFACE.Template.Sessions                       import *
from INTERFACE.Logs.Other_Save_User_Login_out_History  import *

class Sign_out(View):
        def __init__(self,request):
                self.request = request

        def Create_Log(self):
            #-> Creating Log
            Log_Data_List =[]
            ID        = str(Session(self.request).Get_Id())
            User_Name = Session(self.request).Get_Name()
            Operation = "Logout"
            Time      = get_date()
            Date      = get_time()

            Log_Data_List.append(ID)
            Log_Data_List.append(User_Name)
            Log_Data_List.append(Operation)
            Log_Data_List.append(Time)
            Log_Data_List.append(Date)

            Save_User_Login_History().Write_message(Log_Data_List)
            return True
                




								



      	
   
