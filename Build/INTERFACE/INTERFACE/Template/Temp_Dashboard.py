##=> Imports

#=> Lib Import
from django.http.response import HttpResponse,HttpResponsePermanentRedirect, HttpResponseRedirect 
from django.shortcuts     import redirect, render
from django.views         import View

#=> File Import
from  Dashboard.Api.Api_get_data import * 
from  Dashboard.Template.Sessions import *

class Dashboard(View):
    def __init__(self,request):
            self.request = request

    def Dashbord_Page(self):
        Session_Verify = Session(self.request).Verify_Session()
        if(Session_Verify):
            return True
        else:
            return "Session Fail"
        '''result = Session(self.request).Verify_Session()
        if(result):
            Dashboard_data = temp_dashboard(self.request)
            return Dashboard_data
        else:
            False'''

            
            




      	
   
