from django.contrib import admin

from .models import *
# Register your models here.
class DashCommmande(admin.ModelAdmin):
    list_display = ("nbArticle","sommeTotal","nom_client","prenom_client","pseudo_client","addresse_client","telephone_client","date_commande","note")
    search_fields = ("pseudo_client","date_commande","nbArticle",)
    
admin.site.register(Commande,DashCommmande)
