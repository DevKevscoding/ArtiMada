from django.db import models


from datetime import datetime
# Create your models here.
class Commande(models.Model):
    nbArticle = models.IntegerField()
    sommeTotal = models.IntegerField()
    nom_client = models.CharField(max_length=64)
    prenom_client = models.CharField(max_length=64)
    pseudo_client = models.CharField(max_length=64)
    addresse_client = models.CharField(max_length=128)
    telephone_client = models.CharField(max_length=64)
    date_commande = models.DateTimeField(default=datetime.now())
    note = models.TextField()
    