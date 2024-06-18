from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from AppProduit.models import Produit

from datetime import datetime

class Favorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_add = models.DateTimeField(default=datetime.now())
        
    def __str__(self):
        return f"{self.user.username} - {self.produit}"
