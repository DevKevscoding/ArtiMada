from django.shortcuts import render

from .mehode import *

# Create your views here.
def Send(request):
    try:
        if request.method == 'POST':
            nom = request.POST.get("name_email")
            prenom = request.POST.get("forname_email")
            email = str(request.POST.get("email_user"))
            message = request.POST.get("message_email")
            
            subject = f'Nouveau message de {nom} {prenom} .'
            recipient_list = ["ArtiMada@gmail.com"]
            
            sendMail(subject,message,email,recipient_list)
            return render(request,"pages/contact.html",{"message":"Envoyer avec succes"})
    except:
        return render(request,"pages/contact.html",{"error":"Ereur d'envoye "})
        
    