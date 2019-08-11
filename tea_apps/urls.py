
from django.contrib import admin
from django.urls import path
from tea_apps import views
urlpatterns = [
    path('index/',views.Index,name='index'),
    path('reg/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('userinfo/',views.User_info,name='userinfo'),
    path('uinfo/',views.Uinfo,name='uinfo')
]
