from django.urls import path

from .views import *

urlpatterns = [
    path(f'ajout/',pageAjout,name="ajout"),
    path(f'produits/',pageProduit,name="produits"),
    path(f'addProduit/',addProduit,name="addProduit"),
    path(f'pannier/',pagePannier,name="pannier"),
    path(r'show/<int:produit_id>',showDetail,name="show"),
    
    path("remove_pannier/<int:produit_id>",remove_pannier,name="remove"),
    path("pannier/<int:produit_id>",addPannier,name="addpannier"),
    
    path('remove/<int:produit_id>',remove_produit,name="remove_produit"),
    path('update/<int:produit_id>',pageUpdate,name="update"),
    path('modifier/<int:produit_id>',updateProduit,name="modifier"),
    path('successAchat',page_success_achat,name="achatSuccess"),
    
    path('trieCategorie',trieCategorie,name="trieCategorie"),
    path('trieMateriaux',trieMateriaux,name="trieMateriaux"),
    path('rechercheGlobalName',rechercheGlobalName,name="rechercheGlobalName"),
    
]
