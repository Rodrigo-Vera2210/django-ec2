# Generated by Django 4.2.2 on 2023-08-06 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_remove_orden_notas_orden_horometro_alter_orden_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 8, 5, 19, 11, 8, 784864)),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_create',
            field=models.DateField(default=datetime.datetime(2023, 8, 5, 19, 11, 8, 784864)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 5, 19, 11, 8, 784864)),
        ),
    ]
