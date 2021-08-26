"""INTERFACE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from INTERFACE import settings
from django.contrib import admin
from django.urls import path

### => For Debug == OFF
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

#=> My Imports 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    ############-> Template's Paths <-############
    path('',views.index,name='Index'),
    path('Dashboard/',views.dashboard,name='Dashboard'),
    path('Associates/',views.associate,name='Associate'),
    path('Campaign/',views.campaign,name='Campaign'),
    path('User/',views.user,name='User'),
    path('Role/',views.role,name='Role'),
    path('Role Access Details/',views.role_access_details,name='Role Access Details'),
    path('Signout/', views.sign_out, name='Signout'),

    path('Error/',views.error_404_view,name='Error 404'),
    ############-> Visitor Page <-############
    path('Visitor Page',views.visitor_page,name='Visitor Page'),

    #=> For Debug == OFF 

    url(r'^Media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

 ]#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


##=> 404 Page Handler
handler404 = "INTERFACE.views.error_404_view"
##=> 500 Page Handler
handler500 = "INTERFACE.views.error_500_view"
##=> 503 Page Handler
handler503 = "INTERFACE.views.error_503_view"

