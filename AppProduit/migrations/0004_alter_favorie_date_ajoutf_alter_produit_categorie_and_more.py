# Generated by Django 5.0.4 on 2024-05-27 16:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduit', '0003_alter_favorie_date_ajoutf_alter_produit_date_ajout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorie',
            name='date_ajoutF',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 27, 19, 28, 35, 931795), verbose_name="Date d'ajout Notation"),
        ),
        migrations.AlterField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProduit.categorie'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='date_ajout',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 27, 19, 28, 35, 930796)),
        ),
        migrations.AlterField(
            model_name='produit',
            name='materiaux',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProduit.materiaux'),
        ),
    ]
