"""Assignment URL Configuration

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
from django.contrib import admin
from django.urls import path
from UserLoginApp import views as userview
from StudentinfoApp import views as studentview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userview.homepage,name='home'),
    path('signup', userview.signupp, name='signup'),
    path('login', userview.login, name='login'),
    path('changepassword', userview.changepassword, name='changepassword'),
    path('logout', userview.logout, name='logout'),
    path('c_student_info/', studentview.studentcreate, name='c_student_info'),
    path('studentlist/', studentview.studentlist, name='studentlist'),
    path('studentmark/', studentview.studentmark, name='studentmark'),
    path('deletestudentdata/', studentview.deletestudentdata, name='deletestudentdata'),
    path('searchstudent/', studentview.searchstudent, name='search'),
    path('updatepage/', studentview.updatepage, name='updatepage'),
    path('test/', userview.test, name='test'),
]
