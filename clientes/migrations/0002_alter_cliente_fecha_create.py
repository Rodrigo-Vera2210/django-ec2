# Generated by Django 4.2.2 on 2023-08-05 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_create',
            field=models.DateField(default=datetime.datetime(2023, 8, 5, 18, 41, 46, 811472)),
        ),
    ]
