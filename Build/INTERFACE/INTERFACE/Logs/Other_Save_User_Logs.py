##-> Imports

#-> Lib Imports
import csv
import os

#-> File Imports
from Dashboard.Other.Other_Get_Date_and_Time import * 

class Save_User_Logs_History:

    def __init__(self):
         self.File_name = get_date()+".csv"

    def Check_Folder_exist(self):
        try:
            if(os.path.exists("Logs\\Crud_Operations")):
                return True
            else:
                if(os.path.exists("Logs")):
                    os.mkdir(os.getcwd()+"\\Logs\\Crud_Operations")
                    return True
                else:
                    os.mkdir(os.getcwd()+"\\Logs")
                    os.mkdir(os.getcwd()+"\\Logs\\Crud_Operations")
                    return True
        except:
            pass

    def File_exist(self):
        if(os.path.isfile("Logs\\Crud_Operations\\"+self.File_name)):
            return True
        else:
            return False

    def Create_File_and_Write_Columns(self):
        try:
            if(self.Check_Folder_exist()):       
                if not self.File_exist():
                    Columns_Names = ["User_ID","User_Name","Operation Detail","Time","Date"]
                    with open("Logs\\Crud_Operations\\"+self.File_name, 'w',encoding="utf-8") as f:
                        write = csv.writer(f) 
                        write.writerow( Columns_Names)  
                return True
        except:
            pass
               


    def Write_message(self,msg): 
        if(self.File_exist()):
            with open("Logs\\Crud_Operations\\"+self.File_name, 'a',newline='') as f:
                write = csv.writer(f)
                write.writerow(msg)
                write.flush()
                f.close()
        else:
            self.Create_File_and_Write_Columns()
            self.Write_message(msg)

