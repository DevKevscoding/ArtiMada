from django.contrib import admin

from .models import *

# Register your models here.
class DashComs(admin.ModelAdmin):
    list_display = ("commentaire","date","id_membres","id_produit")
    
    class Meta:
        managed = True
        verbose_name = 'Administration des Commentaire'
        verbose_name_plural = 'Administration des Commentaire'
    
admin.site.register(Commentaire,DashComs)