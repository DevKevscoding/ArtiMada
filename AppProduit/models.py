from django.db import models

from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Materiaux(models.Model):
    designation = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return self.designation
    
class Categorie(models.Model):
    type = models.CharField(max_length=64,unique=True)
    
    def __str__(self):
        return self.type
    
class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10,decimal_places=2)
    materiaux = models.CharField(models.ForeignKey(Materiaux, on_delete=models.CASCADE),max_length=64)
    categorie = models.CharField(models.ForeignKey(Categorie, on_delete=models.CASCADE),max_length=64)
    artiste = models.CharField(max_length=100)
    stock = models.IntegerField()
    lieu = models.CharField(max_length=128,default="Antananarivo")
    date_ajout = models.DateTimeField(default=datetime.now())
    description = models.TextField()
    image = models.ImageField(upload_to="static/img/produits")
    
class Favorie(models.Model):
    id_produit = models.IntegerField(models.ForeignKey(Produit, on_delete=models.CASCADE,verbose_name="Produit"))
    id_membre = models.IntegerField(models.ForeignKey(User, on_delete=models.CASCADE))
    notation = models.FloatField(default=0)
    date_ajoutF = models.DateTimeField(default=datetime.now(),verbose_name="Date d'ajout Notation")
    