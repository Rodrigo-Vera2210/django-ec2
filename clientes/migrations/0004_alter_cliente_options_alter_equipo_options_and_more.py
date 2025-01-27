# Generated by Django 4.2.2 on 2023-08-07 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_fecha_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['id'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='equipo',
            options={'ordering': ['id'], 'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_create',
            field=models.DateField(default=datetime.datetime(2023, 8, 7, 15, 3, 29, 411098)),
        ),
    ]
