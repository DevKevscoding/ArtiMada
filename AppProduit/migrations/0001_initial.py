# Generated by Django 5.0.4 on 2024-05-21 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materiaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('artiste', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/img/produits')),
                ('materiaux', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProduit.materiaux')),
            ],
        ),
    ]
