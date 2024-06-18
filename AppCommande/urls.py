from django.urls import path

from .views import *

urlpatterns = [
    path('commande',pageCommade,name="commander"),
    path('procedureStripe',pageStripe,name="procedureStripe"),
    path('successPay',pageSuccess,name="successPay"),
    path(f"effectuer_paiement/",effectuer_paiement,name="effectuer_paiement"),
]
 