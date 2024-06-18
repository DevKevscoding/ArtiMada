from django.shortcuts import render,get_object_or_404

from AppProduit.models import Produit
from .models import Favorie

# Create your views here.
def addFavorie(request,produit_id):
    produit = Produit.objects.get(id=produit_id)
    favorie , created = Favorie.objects.get_or_create(user=request.user , produit=produit)
    if created:
        favoris = Favorie.objects.filter(user=request.user)
        message = f"{produit.nom} a été ajouter à vos favoris."
        context= {
            "message":message,
            'list_favorie':favoris
        }
        
        return render(request,"pages/favorie.html",context)
    else:
        favoris = Favorie.objects.filter(user=request.user)
        error = f"{produit.nom} est déja dans vos favoris."
        context= {
            "error":error,
            'list_favorie':favoris
        }
        return render(request,"pages/favorie.html",context)
    
def afficher_favorie(request):
    try:
        favoris = Favorie.objects.filter(user=request.user)
        context = {'list_favorie':favoris}
        return render(request, 'pages/favorie.html',context)
    except:
        favoris = Favorie.objects.filter(user=request.user)
        context = {'list_favorie':favoris}
        return render(request, 'pages/favorie.html',context)

def remove_favorie(request,produit_id):
    try:
        favorite = get_object_or_404(Favorie,user=request.user,produit=produit_id)
        favorite.delete()
        favoris = Favorie.objects.filter(user=request.user)
        context = {'list_favorie':favoris}
        return render(request,"pages/favorie.html",context)
    except:
        favoris = Favorie.objects.filter(user=request.user)
        context = {'list_favorie':favoris}
        return render(request,"pages/favorie.html",context)
    
