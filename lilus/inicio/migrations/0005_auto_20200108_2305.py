# Generated by Django 2.2.5 on 2020-01-08 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_auto_20200108_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coleccion',
            old_name='nombre_publico',
            new_name='nombre',
        ),
    ]
