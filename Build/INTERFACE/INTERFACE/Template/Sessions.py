##=> Imports


#=> Lib Import
from django.contrib.sessions.models import Session as django_session
import json


class Session():
    def __init__(self,request):
        try:
            self.request     = request
            self.Id          = self.request.session['id']
            self.Name        = self.request.session['name'] 
            self.User_name   = self.request.session['user_name']
            self.Img         = self.request.session['img']
            self.Email       = self.request.session['email']
            self.User_access = self.request.session['user_access']
        except:
            return None

    def Verify_Session(self):
        if (self.request.session.get('user_name',False)):
            return True
        else:
            return False

    def Verify_Page_access(self,name):
        access_list = json.loads(self.User_access)
        page_access = access_list[name]
        if(page_access == "Yes"):
            return True
        else:
            return False

    def Get_Id(self):
        return self.Id
    
    def Get_Name(self):
        return self.Name
    
    def Get_User_name(self):
        return self.User_name
    
    def Get_Img(self):
        return self.Img
    
    def Get_Email(self):
        return self.Email
    
    def Get_User_access(self):
        return self.User_access


    def Delete_Session(self,user_id):      # <---- Delete session if User Account info Update
        id  = []
        key = []

        sessions = django_session.objects.all()
        for i in sessions:
            data = i.get_decoded()
            data = data.get('id')
            id.append(data)
            key.append(str(i))
            
        #-> Create Dic of Session Value
        dct = {}
        for i, j in zip(id, key):
            dct.setdefault(i, []).append(j)
        
        #-> Get Session of that User
        try:
            user_id = int(user_id)
            session_keys = dct[user_id]

            for i in session_keys:
                session = django_session.objects.get(session_key= i)
                django_session.objects.filter(session_key=session).delete()
        except:
            pass
                
        
        return True
        