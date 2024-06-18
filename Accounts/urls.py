from django.urls import path

from .views import *

urlpatterns = [
    path('inscription/',creat_user,name="creat_user"),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('profil/',pageProfil,name="pageProfil"),
    path('sincrire/',formSincrire,name="formsinscrire"),
]
