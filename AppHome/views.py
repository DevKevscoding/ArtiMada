from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User,Group
import os
from django.db import connection
from AppProduit.models import Produit,Categorie,Materiaux

groups = Group.objects.all()

# Create your views here.
def pageAccueuil(request):
    produitPartiel = Produit.objects.order_by('?')[:8]
    
    recent_product = Produit.objects.order_by('-date_ajout')[:4]
    
    context = {"groups":groups,"produitPartiel":produitPartiel,"recent_product":recent_product}
    return render(request,"pages/index.html",context)

def pageConnexion(request):
    return render(request,"pages/connexion.html")

def pageContact(request):
    context = {"produits":Produit.objects.all()}
    return render(request,"pages/contact.html",context)

def pageBlog(request):
    return render(request,"pages/blog.html")

def pageAbout(request):
    return render(request,"pages/about.html")

    