##-> Imports

#-> Lib Imports
import csv
import os

#-> File Imports
from INTERFACE.Other.Other_Get_Date_and_Time import * 


class Save_User_Login_History:

    def __init__(self):
         self.File_name = get_date()+".csv"

    def Check_Folder_exist(self):
        return True
        '''templates\try:
            if(os.path.exists(os.getcwd()+"Logs\\")):
                return True
            else:
                if(os.path.exists(os.getcwd()+"Logs")):
                    os.mkdir(os.getcwd()+"\\Logs\\Login_Logout")
                    return True
                else:
                    os.mkdir(os.getcwd()+"\\Logs")
                    os.mkdir(os.getcwd()+"\\Logs\\Login_Logout")
                    return True
        except:
            pass'''

    def File_exist(self):
        return True
        '''if(os.path.isfile(os.getcwd()+"Logs\\Login_Logout\\"+self.File_name)):
            return True
        else:
            return False'''

    def Create_File_and_Write_Columns(self):
        return True
        '''try:
            if(self.Check_Folder_exist()):
                if not self.File_exist() :
                    Columns_Names = ["User_ID","User_Name","Operation","Time","Date"]
                    with open(os.getcwd()+"Logs\\Login_Logout\\"+self.File_name, 'w',encoding="utf-8") as f:
                        write = csv.writer(f) 
                        write.writerow( Columns_Names)  
                return True
        except:
            pass'''
               
    def Write_message(self,msg):  
        return True
        '''if(self.File_exist()):
            with open(os.getcwd()+"Logs\\Login_Logout\\"+self.File_name, 'a',newline='') as f:
                write = csv.writer(f)
                write.writerow(msg)
                f.close()

        else:
            self.Create_File_and_Write_Columns()
            self.Write_message(msg)'''

        
            


     


