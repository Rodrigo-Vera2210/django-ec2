# Generated by Django 4.2.2 on 2023-08-05 13:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('c_id', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=30)),
                ('direccion', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_create', models.DateField(default=datetime.datetime(2023, 8, 5, 8, 57, 25, 518113))),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('serie', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]