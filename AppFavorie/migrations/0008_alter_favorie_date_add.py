# Generated by Django 5.0.4 on 2024-06-04 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFavorie', '0007_alter_favorie_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorie',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 16, 43, 19, 818497)),
        ),
    ]
