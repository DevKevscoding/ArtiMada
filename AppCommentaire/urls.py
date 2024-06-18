from django.urls import path

from .views import *

urlpatterns = [
     path('insertcoms',insertionComs,name="commenter")
]
