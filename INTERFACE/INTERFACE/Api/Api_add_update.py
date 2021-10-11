###=> This File is Created by M.ROHAN FAROOQUI© 
##=>  This File contains function that allow to verify credentials & get user details after login
##=>  This File contains fucntion that allow to Add/Update Data in Database for User, Associate,Campaign & Role

#=> Lib's
import requests

##=> Variables
default_api_url = "https://wall-of-respect-api.herokuapp.com" #"http://127.0.0.1:5000/"
headers = {"Content-Type":"application/json"}

###########################################################-> Login Page <-###########################################################

###################-> Check Credentials <-###################
def form_verify_credentials(user_name,password):
    url = default_api_url + "/v1/login"
    params =[
        ("User_Name" , user_name),
        ("Password"  , password),
    ]
    resp = requests.post(url,params=params,headers=headers)
    print(resp)
    if(resp.status_code == 200):
        user_login_details = resp.json()[0]
        return user_login_details

    elif(resp.status_code == 401):
        return False

    else:
        return False

###########################################################-> User <-###########################################################

###################-> Add User <-###################
def form_add_user(name,u_name,image_path,email,pswd,role,added_by):
    url = default_api_url + "/v1/user"

    params = [
        ("Name"     ,   name),
        ("User_name", u_name),
        ("Img_path" , image_path),
        ("Email"    , email),
        ("Pswd"     , pswd),
        ("Role"     , role),
        ("Added_by" , added_by),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp

###################-> Update User Info <-###################
def form_update_user_info(name,u_name,img_path,email,role,status,updated_by,user_id):
    url = default_api_url + "/v1/user"

    params = [
        ("Name"      , name),
        ("User_name" , u_name),
        ("Img_path"  , img_path),
        ("Email"     , email),
        ("Role"      , role),
        ("Status"    , status),
        ("Updated_by", updated_by),
        ("User_id"   , user_id),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp


###################-> Update User Pswd <-###################
def form_update_user_pswd(pswd,updated_by,user_id):
    url = default_api_url + "/v1/user"

    params = [
        ("Pswd"      , pswd),
        ("Updated_by", updated_by),
        ("User_id"   , user_id),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp

###########################################################-> Role <-###########################################################

###################-> Add Role's <-###################
def form_add_role(role_name,role_access,added_by):
    url = default_api_url + "/v1/role"

    params = [
        ("Role_name"   , role_name),
        ("Role_access" , role_access),
        ("Added_by"    , added_by),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp

###################-> Update Role <-###################
def form_update_role(role_name,role_access,role_status,updated_by,role_id):
    url = default_api_url + "/v1/role"

    params = [
        ("Role_name"  , role_name),
        ("Role_access", role_access),
        ("Status"     , role_status),
        ("Updated_by" , updated_by),
        ("Roll_id"    , role_id),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp

###########################################################-> Associate  <-###########################################################

###################->  Add Associate  <-###################
def form_add_associate(name,image_url,camp,desig,descrip,quote,added_by):
    url = default_api_url + "/v1/associate"
    params = [
        ("Assc_name" ,  name),
        ("Desig"     ,  desig),
        ("Descrip"   , descrip),
        ("Quote"     , quote),
        ("Img_path"  , image_url),
        ("Camp"      , camp),
        ("Added_by"  , added_by),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp
    

###################-> Update Associate <-###################
def form_update_associate(name,design,Descrip,Moti_Quote,Img_path,Campaign_id,Status,Updated_by,assc_id):
    url = default_api_url + "/v1/associate"
    params = [
        ("Assc_name" , name),
        ("Desig"     , design),
        ("Descrip"   , Descrip),
        ("Quote"     , Moti_Quote),
        ("Img_path"  , Img_path),
        ("Camp_id"   , Campaign_id),
        ("Status"    , Status),
        ("Updated_by", Updated_by),
        ("Assc_id"   , assc_id),
    ]

    resp = requests.post(url,params=params,headers=headers).json()
 
    return resp

###########################################################-> Campaign <-###########################################################

###################-> Add Campaign <-###################
def form_add_campaign(camp_name,added_by):
    url = default_api_url + "/v1/campaign"
    params = [
        ("Camp_name", camp_name),
        ("Added_by" , added_by),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp 

###################-> Update Campaign <-###################
def form_update_campaign(camp_id,camp_name,camp_status,updated_by):
    url = default_api_url + "/v1/campaign"
    params = [
        ("Camp_Id"   , camp_id),
        ("Camp_name" , camp_name),
        ("Status"    , camp_status),
        ("Updated_by", updated_by),
    ]

    resp = requests.post(url,params=params,headers=headers).json()

    return resp