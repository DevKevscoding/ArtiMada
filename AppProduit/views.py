from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import Group,User
import os
from django.db import connection

from .models import *

groups = Group.objects.all()
list_categorie = Categorie.objects.all()
list_materiaux = Materiaux.objects.all()

# Create your views here.
def pageAjout(request):
    context= {"list_categorie":list_categorie,"list_materiaux":list_materiaux}
    return render(request,"pages/ajout.html",context)

def pageProduit(request):
    produitAll = Produit.objects.all()
    
    context = {
        "produitAll":produitAll,
        "list_categorie":list_categorie,
        "list_materiaux":list_materiaux
    }
    return render(request,"pages/produits.html",context)

def uploadImages(request,em):
    if "imageProduit" in request.FILES:
        fichier = request.FILES["imageProduit"]
        extansion = os.path.splitext(fichier.name)
        
        newname = f"{em}{extansion[1]}"
        
        emplacement = os.path.join("static/img/produits/",newname)
        
        with open(emplacement,'wb') as destination:
            for chunk in fichier.chunks():
                destination.write(chunk)
    
    return newname
    
def addProduit(request):
        if request.method == 'POST':
            nomProduit = request.POST.get('nomProduit')
            categorie = request.POST.get('categorie')
            materiaux = request.POST.get('materiaux')
            lieu = request.POST.get('lieu')
            prix = request.POST.get('prix')
            stock = request.POST.get('stock')
            artisan = request.POST.get('artisan')
            description = request.POST.get('description')
            
            ProduiExist = Produit.objects.filter(nom = nomProduit)
            nbProduitExiste = len(ProduiExist)
            
            if int(stock) > 0 and int(prix) > 0:
                if nbProduitExiste == 0:
                    upload = uploadImages(request,nomProduit)
                    insertion = Produit(
                        nom = nomProduit,
                        prix = prix,
                        materiaux = materiaux,
                        categorie = categorie,
                        artiste = artisan,
                        stock = stock,
                        lieu = lieu,
                        description = description,
                        image = f'static/img/produits/{ upload }',
                    )
                    insertion.save()
                    context = {"message":"L'ajout dans le catalogue est un success .","list_categorie":list_categorie,"list_materiaux":list_materiaux}
                    return render(request,"pages/ajout.html",context)
                
            else:
                context = {"error":"Il y des valeurs negatifs ou null dans les champs .","list_categorie":list_categorie,"list_materiaux":list_materiaux}
                return render(request,"pages/ajout.html",context)
            
def showDetail(request,produit_id):
    prod = Produit.objects.get(pk=produit_id)
    membre = Produit.objects.all()
    id_produit = produit_id
    
    with connection.cursor() as cursor:
        
        cursor.execute("""
            SELECT DISTINCT Appcommentaire_commentaire.*, auth_user.*,Accounts_profile.*
            FROM Appcommentaire_commentaire
            JOIN auth_user ON Appcommentaire_commentaire.id_membres = auth_user.id
            JOIN Accounts_profile ON auth_user.id = (Accounts_profile.id)+1
            WHERE Appcommentaire_commentaire.id_produit = %s
        """,[id_produit])
        
        comments = cursor.fetchall()
        content = {
            "produit":prod,
            "coms":comments,
            "nbcoms":len(comments),
            "membres":membre
        }
    
    context = {"article":get_object_or_404(Produit, pk=produit_id),"content":content}
    return render(request,"pages/detail.html",context)

def pagePannier(request):   
    return render(request,"pages/pannier.html")

def addPannier(request, produit_id):
    produit = Produit.objects.get(pk=produit_id)
    
    if "pannier" not in request.session:
        request.session["pannier"] = []
        
    pannier = request.session["pannier"]
    unique_key = int(produit.id)
    
    obj = {
        "id_produit":unique_key,
        "nom":produit.nom,
        "image":str(produit.image),
        "prix":int(produit.prix),
        "stock":produit.stock,
    }
    
    if obj not in pannier:
        pannier.append(obj)
        request.session.modified = True
    
    context = {"produits": get_object_or_404(Produit, pk=produit_id),"produit_id":produit_id}
    return render(request, "pages/pannier.html",context)

def remove_pannier(request, produit_id):
    if 'pannier' in request.session:
        pannier = request.session['pannier']
        for index,prod in enumerate(pannier):
            if prod['id_produit'] == produit_id:
                del pannier[index]
                break
        request.session['pannier'] = pannier
        
    context = {"id":id} 
        
    return render(request, "pages/pannier.html",context)

def remove_produit(request, produit_id):
    produitAll = Produit.objects.all()
    
    context = {
        "produitAll":produitAll
    }
    produit  = Produit.objects.get(pk = produit_id)
    produit.delete()
    return render(request,"pages/produits.html",context)

def pageUpdate(request, produit_id):
    produit = Produit.objects.get(pk = produit_id)
    context = {
        "article":produit,
        "list_categorie":list_categorie,
        "list_materiaux":list_materiaux,
    }
    return render(request,"pages/update.html",context)

def updateProduit(request, produit_id):
    if request.method == 'POST':
        nomUp = request.POST.get("nom_update")
        categorieUp = request.POST.get("categorie_update")
        materiauxUp = request.POST.get("materiaux_update")
        lieuUp = request.POST.get("lieu_update")
        prixUp = request.POST.get("prix_update")
        stockUp = request.POST.get("stock_update")
        descriptionUp = request.POST.get("description_update")
        
        id_produit = request.POST.get("id_produit")
        
        produit = Produit.objects.get(pk=id_produit)
        
        produit.nom = nomUp
        produit.categorie = categorieUp
        produit.materiaux = materiauxUp
        produit.lieu = lieuUp
        produit.prix = prixUp
        produit.stock = stockUp
        produit.description = descriptionUp
        
        produit.save()
        
        produitAll = Produit.objects.all()
    
        context = {
            "produitAll":produitAll
        }
        
    return render(request,"pages/produits.html",context)

def trieCategorie(request):
    
    trie_categorie = request.POST.get("trie_categorie")
    
    produitAll = Produit.objects.all().filter(categorie=trie_categorie)
    
    context = {
            "produitAll":produitAll,
            "list_categorie":list_categorie,
            "list_materiaux":list_materiaux
        }
        
    return render(request,"pages/produits.html",context)

def trieMateriaux(request):
    
    trie_materiaux = request.POST.get("trie_materiaux")
    
    produitAll = Produit.objects.all().filter(materiaux=trie_materiaux)
    
    context = {
            "produitAll":produitAll,
            "list_categorie":list_categorie,
            "list_materiaux":list_materiaux
        }
        
    return render(request,"pages/produits.html",context)

def rechercheGlobalName(request):
    resultat = request.POST.get("search_value")
    if resultat:
        values = Produit.objects.filter(nom__icontains=resultat)
        
        context = {
            "produitAll":values,
            "list_categorie":list_categorie,
            "list_materiaux":list_materiaux
        }
        
        return render(request,"pages/produits.html",context)
    
def page_success_achat(request):
    return render(request,"pages/success_payement.html")


    
    