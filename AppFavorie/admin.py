from django.contrib import admin

from .models import Favorie

# Register your models here.

@admin.register(Favorie)
class DashFavorie(admin.ModelAdmin):
    list_display = ("user","produit","date_add")
