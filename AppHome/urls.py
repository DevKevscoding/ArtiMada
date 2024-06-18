from django.urls import path
from .views import *

urlpatterns = [
    path('',pageAccueuil,name="pageAcceuil"),
    path('connexion/',pageConnexion,name="connexion"),
    path('contact/',pageContact,name="contact"),
    path('blog/',pageBlog,name="blog"),
    path('about/',pageAbout,name="about")
]
