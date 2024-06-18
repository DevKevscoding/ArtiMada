from django.db import models
from django.contrib.auth.models import User
from AppProduit.models import Produit

# Create your models here.
class Commentaire(models.Model):
    id_produit = models.IntegerField(models.ForeignKey(Produit, on_delete=models.CASCADE))
    id_membres = models.IntegerField(models.ForeignKey(User, on_delete=models.CASCADE))
    commentaire = models.TextField()
    date = models.DateField()