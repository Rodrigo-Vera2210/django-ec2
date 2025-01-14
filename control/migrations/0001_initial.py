# Generated by Django 4.2.2 on 2023-08-05 13:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('causas', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('modelo', models.CharField(blank=True, max_length=20, null=True)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('unidad', models.CharField(max_length=10)),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('date', models.DateField(default=datetime.datetime(2023, 8, 5, 8, 57, 25, 521316))),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_create', models.DateField(default=datetime.datetime(2023, 8, 5, 8, 57, 25, 522325))),
                ('fecha', models.DateField(default=datetime.datetime(2023, 8, 5, 8, 57, 25, 522325))),
                ('tipo', models.CharField(default='preventivo', max_length=50)),
                ('lugar', models.CharField(default='taller matriz', max_length=50)),
                ('estado', models.BooleanField(default=False)),
                ('aprobacion', models.BooleanField(default=False)),
                ('observacion', models.TextField(blank=True, max_length=250, null=True)),
                ('recomendacion', models.TextField(blank=True, max_length=250, null=True)),
                ('tecnico', models.CharField(max_length=50)),
                ('recibe', models.CharField(max_length=50)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('notas', models.TextField(blank=True, max_length=100, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('orden', models.ForeignKey(default=9999, on_delete=django.db.models.deletion.CASCADE, to='control.orden')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='detalleProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('orden', models.ForeignKey(default=9999, on_delete=django.db.models.deletion.CASCADE, to='control.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCausas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='causas.causas')),
                ('orden', models.ForeignKey(default=9999, on_delete=django.db.models.deletion.CASCADE, to='control.orden')),
            ],
        ),
    ]
