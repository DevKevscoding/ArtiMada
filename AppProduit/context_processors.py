from django.contrib.auth.models import Group,User
from .models import *

groups = Group.objects.all()
list_materiaux = Materiaux.objects.all()

def list_categorie_global(request):
    data = Categorie.objects.all()
    my_global_dic = {item.id:item.type for item in data}
    return { 'my_global_categorie':my_global_dic }