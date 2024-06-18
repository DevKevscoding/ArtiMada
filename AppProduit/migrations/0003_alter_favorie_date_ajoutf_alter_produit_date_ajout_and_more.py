# Generated by Django 5.0.4 on 2024-05-27 16:23

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduit', '0002_categorie_favorie_produit_categorie_produit_lieu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorie',
            name='date_ajoutF',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 27, 19, 23, 42, 908836), verbose_name="Date d'ajout Notation"),
        ),
        migrations.AlterField(
            model_name='produit',
            name='date_ajout',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 27, 19, 23, 42, 907838)),
        ),
        migrations.AlterField(
            model_name='produit',
            name='materiaux',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProduit.categorie'),
        ),
    ]
