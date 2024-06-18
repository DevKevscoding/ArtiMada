from django.urls import path

from .views import *

urlpatterns = [
    path("sendMail",Send,name="sendMail")
]
