from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    email = models.EmailField(max_length=254, unique=True)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL, null=True,blank=True)
    photo = models.ImageField(upload_to='static/img/user')
    
    def __str__(self):
        return self.user.username
    