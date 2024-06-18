from django.shortcuts import render,get_list_or_404
from .models import Profile
from django.contrib.auth.models import Group,User
import os
from django.contrib.auth import authenticate, login, logout
from AppProduit.views import *

groups = Group.objects.all()

# Create your views here.
def uploadPhoto(request,em):
    if "myphoto" in request.FILES:
        fichier = request.FILES["myphoto"]
        extansion = os.path.splitext(fichier.name)
        
        newname = f'{em}{extansion[1]}'
        
        emplacement = os.path.join("static/img/user/",newname)
        
        with open(emplacement,'wb') as destination:
            for chunk in fichier.chunks():
                destination.write(chunk)
                
    return newname
                
def creat_user(request):
    if request.method == 'POST':
        username = request.POST.get('pseudo')
        email_inscription = request.POST.get('email')
        password_inscription = request.POST.get('password')
        password_conf = request.POST.get('password_conf')
        group_id = request.POST.get('groupe')
        
        upload = uploadPhoto(request,email_inscription)
        photo = f'static/img/user/{upload}'
        
        emailExist = User.objects.filter(email=email_inscription)
        pseudoExist = User.objects.filter(username=username)
        produitPartiel = Produit.objects.order_by('?')[:8]
        recent_product = Produit.objects.order_by('-date_ajout')[:4]
        nbEmail = len(emailExist)
        nbPseudo = len(pseudoExist)
        
        try:
            if nbEmail == 0:
                if nbPseudo == 0:
                    if password_inscription == password_conf:
                        print(upload)
                        print(photo)
                        if upload != None:
                            user = User.objects.create_user(
                            username = username,
                            password = password_inscription,
                            email=email_inscription,    
                            )
                            group = Group.objects.get(id=group_id)
                            recent_product = Produit.objects.order_by('-date_ajout')[:4]
                            
                            profil, created = Profile.objects.get_or_create(user=user,email=email_inscription,photo=photo)
                            profil.group = group
                            profil.save()
                            
                            group.user_set.add(user)
                            
                            context = {"message":"Inscription avec success","groups":groups,"recent_product":recent_product,"produitPartiel":produitPartiel}
                            
                            return render(request,"pages/index.html",context)
                        else:
                            recent_product = Produit.objects.order_by('-date_ajout')[:4]
                            error_message = "Erreur durant l'importation de la photo."
                            context = {"error_message":error_message,"groups":groups,"recent_product":recent_product,"produitPartiel":produitPartiel}
            
                            return render(request,"pages/index.html",context)
                    else:
                        error_message = "Le mot de passe de confirmation est incorrect."
                        context = {"error_message":error_message,"groups":groups,"recent_product":recent_product,"produitPartiel":produitPartiel}
        
                        return render(request,"pages/index.html",context)
                    
                else:
                    error_message = "Le Pseudo est déja utilier par un autre membre."
                    context = {"error_message":error_message,"groups":groups,"recent_product":recent_product,"produitPartiel":produitPartiel}
    
                    return render(request,"pages/index.html",context)
            else:
                error_message = "L'Email est dèja utiliser par un autre membre."
                context = {"error_message":error_message,"groups":groups,"produitPartiel":produitPartiel,"recent_product":recent_product}
    
                return render(request,"pages/index.html",context)
                    
        except:
            error_message = "Il s'est produit une erreur !"
            context = {"error_message":error_message,"groups":groups}
    
            return render(request,"pages/index.html",context)
            
def login_user(request):
    produitPartiel = Produit.objects.all()[:8]
    try:
        if request.method == 'POST':
            pseudo = request.POST.get("login_pseudo")
            pwd = request.POST.get("login_pwd")
            
            user = authenticate(username=pseudo, password=pwd)
            profil_member = Profile.objects.get(user=user)
            if user is not None:
                login (request, user)
                return render(request,"pages/profil.html")
    except:
        context = {"message_eroor":"Pseudo ou mot de passe invalide !"}
        return render(request,"pages/connexion.html",context)
    
def logout_user(request):
    produitPartiel = Produit.objects.all()[:8]
    logout(request)
    recent_product = Produit.objects.order_by('-date_ajout')[:4]
    context = {"groups":groups,"produitPartiel":produitPartiel,"recent_product":recent_product} 
    return render(request,"pages/index.html",context)

def pageProfil(request):
    return render(request,"pages/profil.html")

def formSincrire(request):
    produitPartiel = Produit.objects.order_by('?')[:8]
    
    recent_product = Produit.objects.order_by('-date_ajout')[:4]
    
    context = {"groups":groups,"produitPartiel":produitPartiel,"recent_product":recent_product}
    return render(request,"pages/index.html",context)