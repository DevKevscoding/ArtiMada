# Generated by Django 5.0.4 on 2024-06-04 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProduit', '0012_alter_favorie_date_ajoutf_alter_produit_date_ajout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorie',
            name='date_ajoutF',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 16, 43, 19, 814918), verbose_name="Date d'ajout Notation"),
        ),
        migrations.AlterField(
            model_name='produit',
            name='date_ajout',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 16, 43, 19, 813920)),
        ),
    ]
