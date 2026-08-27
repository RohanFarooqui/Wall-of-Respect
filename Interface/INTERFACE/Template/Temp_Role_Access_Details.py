##=> Imports

#=> Lib Import
from django.http.response import HttpResponse,HttpResponsePermanentRedirect, HttpResponseRedirect 
from django.shortcuts     import redirect, render
from django.views         import View

#=> File Import
from  INTERFACE.Api.Api_get_data  import * 
from  INTERFACE.Template.Sessions import *

class Role_Access_Details(View):
    def __init__(self,request):
            self.request = request

    def Role_Access_Page(self):
        session_check = Session(self.request).Verify_Session()
        if(session_check):
            if(Session(self.request).Verify_Page_access('role_page')):
                return True
            else:
                return "Page Access Not Allowed"
        else:
            return "Session Fail"
            