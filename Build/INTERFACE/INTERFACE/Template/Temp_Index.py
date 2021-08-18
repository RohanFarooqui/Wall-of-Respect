##=> Imports

#=> Lib Import
from django.http.response import HttpResponse,HttpResponsePermanentRedirect, HttpResponseRedirect 
from django.shortcuts     import redirect, render
from django.views.generic import TemplateView
from django.views         import View
from django.contrib       import messages


#=> File Import
from Dashboard.Api.Api_add_update                      import * 
from Dashboard.Template.Sessions					   import *
from Dashboard.Logs.Other_Save_User_Login_out_History  import *

class Index(View):
	def __init__(self,request):
		self.request = request

	def Login(self):
		if(self.request.method == 'POST'):
			#-> Get First Name
			name = self.request.POST['username']
			#-> Password 
			pswd = self.request.POST['password']
			#-> Remember me
			remember_me = self.request.POST.getlist('remember-me')

			#-> Send Data to API & Get Response
			result_1 = form_verify_credentials(name,pswd)
			if result_1 != False:				
				self.request.session['id']          = result_1[0]
				self.request.session['name']        = result_1[1]
				self.request.session['user_name']   = result_1[2]
				self.request.session['img']         = result_1[3]
				self.request.session['email']       = result_1[4]
				self.request.session['user_access'] = result_1[5]

				if 'remember_me' in remember_me:
					self.request.session.set_expiry(1209600)
				else:
					self.request.session.set_expiry(0)

				#-> Create Log
				self.Write_log_message()

				return True
			else:
				messages.error(self.request,"Incorrect email or password!")
				return False	
		else:
			return False
		

	#-> Write Log to csv
	def Write_log_message(self):
		try:
			#-> Creating Log
			Log_Data_List =[]
			ID        = str(Session(self.request).Get_Id())
			User_Name = Session(self.request).Get_Name()
			Operation = "Login"
			Time      = get_date()
			Date      = get_time()

			Log_Data_List.append(ID)
			Log_Data_List.append(User_Name)
			Log_Data_List.append(Operation)
			Log_Data_List.append(Time)
			Log_Data_List.append(Date)

			Save_User_Login_History().Write_message(Log_Data_List)
		except:
			pass


      	
   
