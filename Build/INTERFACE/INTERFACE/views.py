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
