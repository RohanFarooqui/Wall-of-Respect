###=> This File is Created by M.ROHAN FAROOQUI© 
##=>  This File function take sesion values & data from API's
##=>  It send this as dictionary to frontend Template

#=> Lib's
import requests
import json 

#=> File Import
from INTERFACE.Template.Sessions import *

#=> Variables
default_api_url = "http://127.0.0.1:5000/"#"https://wall-of-respect-api.herokuapp.com/"


####################-> Dashboard <-####################
def temp_dashboard(request):
    global default_api_url

    get_session_val   =  Session(request)

    context = {
        "Id"               : get_session_val.Get_Id(),
        "Name"             : get_session_val.Get_Name(),
        "User_Name"        : get_session_val.Get_User_name(),
        "Img_url"          : get_session_val.Get_Img(),
        "Email"            : get_session_val.Get_Email(),
        "User_access"      : json.loads(get_session_val.Get_User_access()),
        "Total_Users"      : (requests.get(default_api_url + "/v1/total-user")).text,
        "Total_Roles"      : (requests.get(default_api_url + "/v1/total-role")).text,
        "Total_Associates" : (requests.get(default_api_url + "/v1/total-associate")).text,
        "Total_Campaign"   : (requests.get(default_api_url + "/v1/total-campaign")).text,
        "Recent_Associates": (requests.get(default_api_url + "/v1/associate")).json()[-4:],
        "Recent_Users"     : (requests.get(default_api_url + "/v1/user")).json()[-3:],
        "Recent_Campaigns" : (requests.get(default_api_url + "/v1/campaign")).json()[-5:],
        "Recent_Roles"     : (requests.get(default_api_url + "/v1/role")).json()[-4:],
    }

    return context

####################-> Associate <-####################
def temp_associate(request):
    global default_api_url
    ##-> Get Session Values
    get_session_val   =  Session(request)
    ##-> Get Associate's Data
    Associate_List = (requests.get(default_api_url + "/v1/associate")).json()
    ##-> Get Design List
    Design_List=[]
    
    try:
        a=[ x[2] for x in Associate_List]
        for i in a:
            if i not in Design_List:
                Design_List.append(i)
    except:
        pass
     
    context = {
        "Id"              : get_session_val.Get_Id(),
        "Name"            : get_session_val.Get_Name(),
        "User_Name"       : get_session_val.Get_User_name(),
        "Img_url"         : get_session_val.Get_Img(),
        "Email"           : get_session_val.Get_Email(),
        "User_access"     : json.loads(get_session_val.Get_User_access()),
        "Associates_List" : Associate_List,
        "Campaigns_List"  : (requests.get(default_api_url + "/v1/campaign")).json(),
        "Designation_list": Design_List,
    }
    return context

####################-> Campaign <-####################
def temp_campaign(request):
    global default_api_url
    
    get_session_val   =  Session(request)

    context = {
        "Id"             : get_session_val.Get_Id(),
        "Name"           : get_session_val.Get_Name(),
        "User_Name"      : get_session_val.Get_User_name(),
        "Img_url"        : get_session_val.Get_Img(),
        "Email"          : get_session_val.Get_Email(),
        "User_access"    : json.loads(get_session_val.Get_User_access()),  
        "Campaigns_List" : (requests.get(default_api_url + "/v1/campaign")).json(),
    }
    return context

####################-> User <-####################
def temp_user(request):
    global default_api_url
    
    get_session_val   =  Session(request)

    context = {
        "Id"           : get_session_val.Get_Id(),
        "Name"         : get_session_val.Get_Name(),
        "User_Name"    : get_session_val.Get_User_name(),
        "Img_url"      : get_session_val.Get_Img(),
        "Email"        : get_session_val.Get_Email(),
        "User_access"  : json.loads(get_session_val.Get_User_access()),    
        "User_List"    : (requests.get(default_api_url + "/v1/user")).json(),
        "Role_List"    : (requests.get(default_api_url + "/v1/role")).json(),
    }
    return context

####################-> Role <-####################
def temp_role(request):
    global default_api_url
    
    get_session_val   =  Session(request)

    context = {
        "Id"           : get_session_val.Get_Id(),
        "Name"         : get_session_val.Get_Name(),
        "User_Name"    : get_session_val.Get_User_name(),
        "Img_url"      : get_session_val.Get_Img(),
        "Email"        : get_session_val.Get_Email(),
        "User_access"  : json.loads(get_session_val.Get_User_access()),      
        "Role_List"    : (requests.get(default_api_url + "/v1/role")).json(),
    }
    return context

def temp_role_access_details(request):
    global default_api_url

    get_session_val   =  Session(request)

    Role = (requests.get(default_api_url + "/v1/role")).json()

    acces_list = []
    for i in Role:
        temp = []
        for j in range(0,len(i)):
            if(j==2):
                a= json.loads(i[j])
                for k in a:
                    temp.append(a.get(k))
            else:
                temp.append(i[j])
        acces_list.append(temp)

    context = {
        "Id"           : get_session_val.Get_Id(),
        "Name"         : get_session_val.Get_Name(),
        "User_Name"    : get_session_val.Get_User_name(),
        "Img_url"      : get_session_val.Get_Img(),
        "Email"        : get_session_val.Get_Email(),
        "User_access"  : json.loads(get_session_val.Get_User_access()),
        "Role_List"    : acces_list,
    }
    return context

####################-> Visotor Page <-####################

def temp_visitor_page():
    assc_data = requests.get(default_api_url + "/v1/associate").json()

    assc_date_dic =[]
    for i in assc_data:
        d = []
        if(i[7] == '1'):
            d.append(i[0])
            d.append(i[1])
            d.append(i[2])
            d.append(i[3])
            d.append(i[4])
            d.append(i[5])
            d.append(i[6])
            d.append(i[7])
        if(len(d) > 0):
            assc_date_dic.append(d)

    context = {         
        "Associates_List_1": assc_date_dic,
    }

    return context


     