# Generated by Django 2.2.5 on 2020-01-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20200108_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='coleccion',
            name='activa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coleccion',
            name='tipo',
            field=models.CharField(choices=[('Evento', 'Evento'), ('Comunion', 'Comunión'), ('Bautizo', 'Bautizo'), ('Verano', 'Verano')], default='Evento', max_length=32),
        ),
    ]
