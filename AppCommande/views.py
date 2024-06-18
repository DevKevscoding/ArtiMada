from django.shortcuts import render

from .models import *
from dotenv import load_dotenv
import stripe
import os

load_dotenv()

stripe.api_key = os.environ.get("SECRET_KEY")

# Create your views here.
def pageCommade(request):
    if request.method == 'POST':
        nbArticle = request.POST.get("nbArticle")
        totalSomme = request.POST.get("totalSomme")
        
        context = {
            "nbArticle":nbArticle,
            "totalSomme":totalSomme
        }
        return render(request,"pages/commande.html",context)
    
def pageStripe(request):
    if request.method == 'POST':
        nbArticle = request.POST.get("nbArticle_commande")
        sommetotal = request.POST.get("sommeTotal_commande")
        pseudo = request.POST.get("pseudo_commande")
        nom = request.POST.get("nom_commande")
        prenom = request.POST.get("prenom_commande")
        addresse = request.POST.get("adresse_commande")
        telephone = request.POST.get("telephone_commande")
        note = request.POST.get("note_client")
        
        # insertion = Commande(
        #     nbArticle = nbArticle,
        #     sommeTotal = sommetotal,
        #     nom_client = nom,
        #     prenom_client = prenom,
        #     pseudo_client = pseudo,
        #     addresse_client = addresse,
        #     telephone_client = telephone,
        #     note = note
        # )
        # insertion.save()
        
        context = {
            "prenom":prenom,
            "nom":nom,
            "addresse":addresse,
            "sommetotal":sommetotal,
        }
        
        return render(request,"pages/procedureStripe.html",context)

def pageSuccess(request):
    return render(request,"pages/success_payement.html")

def effectuer_paiement(request):
    if request.method == 'POST':
        total_prix = request.POST.get("prixtotal")
        token = request.POST.get("stripeToken")
        print([token,total_prix])
        try:
            # Créer une charge avec Stripe en utilisant le token
            charge = stripe.Charge.create(
                amount=int(total_prix) * 100,
                currency="usd",
                source=token,
                description="Votre commande est un success"
            )
            
            # Si la charge est réussie, afficher un message de succès
            return render(request, "pages/success_payement.html", {"message": "Paiement réussi !"})
        except stripe.error.StripeError as e:
            error = "Une erreur s'est produite lors du traitement de votre paiement. Veuillez réessayer plus tard."
            print(e)
            return render(request, "pages/success_payement.html", {"error": error})
    else:
        error = "Une erreur s'est produite lors du traitement de votre paiement. Veuillez réessayer plus tard."
        return render(request, "pages/success_payement.html", {"error": error})