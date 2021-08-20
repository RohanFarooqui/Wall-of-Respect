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
        if Dashboard_page:
            return render(request,'Dashboard.html',context= Dashboard_data)
        elif(Dashboard_page == "Session Fail"):
            return redirect('/Signout')
        else:
            return redirect('/Signout')
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
