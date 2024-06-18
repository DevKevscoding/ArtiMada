from django.shortcuts import render,redirect
from .models import *

from datetime import datetime

# Create your views here.
def insertionComs(request):
    if request.method == 'POST':
        id_membre = request.POST.get("id_membre")
        id_pro = request.POST.get("id_produit")
        coms = request.POST.get("coms")
        timestamp = datetime.now().strftime("%Y-%m-%d")

        
        if coms != "":
            insert = Commentaire(
                id_produit = id_pro,
                id_membres = id_membre,
                commentaire = coms,
                date = timestamp
            )    
            insert.save()
            return redirect(f'http://127.0.0.1:8000/show/{id_pro}',{"message":"Commentaire envoyer."})
        else:
            return redirect(f'http://127.0.0.1:8000/show/{id_pro}',{"message":"Champs Commentaire aubliguatoire."})