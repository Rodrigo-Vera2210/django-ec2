# Generated by Django 4.2.2 on 2023-08-07 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('causas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='causas',
            options={'ordering': ['id'], 'verbose_name': 'Causa', 'verbose_name_plural': 'Causas'},
        ),
    ]
