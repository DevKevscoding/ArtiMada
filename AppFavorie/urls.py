from django.urls import path

from .views import *

urlpatterns = [
    path('ajoutFavorie/<int:produit_id>',addFavorie,name="ajouterFavorie"),
    path('listeFavorie',afficher_favorie,name="list_favorie"),
    path('removeFavorie/<int:produit_id>',remove_favorie,name="removeFavorie"),
]
