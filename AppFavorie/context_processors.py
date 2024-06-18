from django.shortcuts import render,redirect
from .models import Favorie

def vue_prossecor(request):
    try:
        if request.user.is_authenticated:
            nb_favorie = Favorie.objects.all().filter(user=request.user).count()
            return {
                'count_favorie':request.session.get('count_favorie',nb_favorie)
            }
        else:
            return {
                'count_favorie':request.session.get('count_favorie',0)
            }
    except:
        return {
                'count_favorie':request.session.get('count_favorie',0)
            }
    