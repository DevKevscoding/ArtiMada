# Generated by Django 5.0.4 on 2024-05-28 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFavorie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorie',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 16, 30, 47, 474568)),
        ),
    ]
