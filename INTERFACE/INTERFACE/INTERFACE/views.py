###=> This File is Created by M.ROHAN FAROOQUI© 
##=> The Views.py Render html files template's

##=> Django Imports
from django.http.response      import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts          import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib            import messages

##-> Files Import

#=> Api Class
from .Api.Api_add_update import *
from .Api.Api_get_data   import *

#=> Template Class
from .Template.Temp_Index               import *
from .Template.Temp_Dashboard           import *
from .Template.Temp_Associate           import *
from .Template.Temp_Campaign            import *
from .Template.Temp_User                import *
from .Template.Temp_Role                import *
from .Template.Temp_Role_Access_Details import *
from .Template.Temp_Signout             import*

##-> Other Libs
from datetime import datetime
import json
import os 

###########################-> Templates Render Functions <-#########################

####################-> Index <-####################
def index(request):
    index_page = Index(request).Login()
    session_check = Session(request).Verify_Session()
    if session_check:
        return redirect('/Dashboard')
    else:
        return render(request,"Index.html")
    return render(request,"Index.html")

####################-> Dashboard <-####################
def dashboard(request):
    session_check = Session(request).Verify_Session()
    if  session_check:
        Dashboard_page = Dashboard(request).Dashbord_Page()
        Dashboard_data = temp_dashboard(request)
        if (Dashboard_page):
            return render(request,'Dashboard.html',context= Dashboard_data)
        elif(Dashboard_page == "Session Fail"):
            return redirect('/Signout')
        else:
            return render('/Dashboard',context= Dashboard_data)
    else:
        return redirect('/')

####################-> Associate <-####################
def associate(request):
    session_check = Session(request).Verify_Session()
    if  session_check:
        Associate_page = Associate(request).Associate_Page()
        Associate_Data = temp_associate(request)
        if(not Associate_page):
            return render(request,'Associate.html',context=Associate_Data ) 
        elif(Associate_page == "Page Access Not Allowed"):
            return redirect("/Error")
        elif(Associate_page == "Session Fail"):
            return redirect('/Signout')
        else:
            return redirect('/Associates',context=Associate_Data ) 
    else:
        return redirect('/')

####################-> Campaign <-####################
def campaign(request):
    session_check = Session(request).Verify_Session()
    if  session_check:
        Campaign_page = Campaign(request).Campaign_Page()
        Campaign_Data = temp_campaign(request)
        if(not Campaign_page):
            return render(request,'Campaign.html',context=Campaign_Data ) 
        elif(Campaign_page == "Page Access Not Allowed"):
            return redirect("/Error")
        elif(Campaign_page == "Session Fail"):
            return redirect('/Signout')
        else:
            return redirect('/Campaign',context=Campaign_Data ) 
    else:
        return redirect('/')

####################-> User <-####################
def user(request):
    session_check = Session(request).Verify_Session()
    if  session_check:
        User_page = User(request).User_Page()
        User_Data = temp_user(request)
        if(not User_page):
            return render(request,'User.html',context=User_Data ) 
        elif( User_page == "Page Access Not Allowed"):
            return redirect("/Error")
        elif( User_page == "Session Fail"):
            return redirect('/Signout')
        else:
            return redirect('/User',context=User_Data ) 
    else:
        return redirect('/')

####################-> Role <-####################
def role(request):
    session_check = Session(request).Verify_Session()
    if  session_check:
        Role_page = Role(request).Role_Page()
        Role_Data = temp_role(request)
        if(not Role_page):
            return render(request,'Role.html',context=Role_Data ) 
        elif(Role_page == "Page Access Not Allowed"):
            return redirect("/Error")
        elif(Role_page == "Session Fail"):
            return redirect('/Signout')
        else:
            return redirect('/Role',context=Role_Data ) 
    else:
        return redirect('/')

def role_access_details(request):
    session_check = Session(request).Verify_Session()
    if  session_check:
        Role_access_details_page = Role_Access_Details(request).Role_Access_Page()
        Role_access_details_data = temp_role_access_details(request)
        if not Role_access_details_page:
            return render(request,'Role Access Level.html',context= Role_access_details_data) 
        elif(Role_access_details_page  == "Page Access Not Allowed"):
            return redirect("/Error")
        elif(Role_access_details_page == "Session Fail"):
            return redirect('/Signout')
        else:
            return render(request,'Role Access Level.html',context= Role_access_details_data) 
    else:
        return redirect('/')


####################-> Signout  <-####################
def sign_out(request):
    Sign_out(request).Create_Log()
    return redirect('/')

####################-> Error 404  <-####################
def error_404_view(request,exception=None):
    return render(request,"404.html")

####################-> Error 500  <-####################
def error_500_view(request,*args, **argv):
    return render(request,"500.html")

####################-> Error 503  <-####################
def error_503_view(request,*args, **argv):
    return render(request,"503.html")


####################-> Vistor Page  <-####################
def visitor_page(request):
    return render(request,'Visitor.html',context=temp_visitor_page())


