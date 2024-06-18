from django.contrib import admin
from .models import Produit,Materiaux,Categorie,Favorie

# Register your models here.
@admin.register(Materiaux)
class DashMateriaux(admin.ModelAdmin):
    list_display = ("designation",)
    
@admin.register(Produit)
class DashProduit(admin.ModelAdmin):
    list_display = ("id","nom","prix","materiaux","categorie","date_ajout","description",)
    search_fields = ("nom","materiaux","categorie",)
    list_filter = ("materiaux",)
   
@admin.register(Categorie) 
class DashCategorie(admin.ModelAdmin):
    list_display = ("type",)
    
@admin.register(Favorie)
class DashFavorie(admin.ModelAdmin):
    list_display = ("id_produit","id_membre","notation","date_ajoutF",)
    search_fields = ("notation",)
    

