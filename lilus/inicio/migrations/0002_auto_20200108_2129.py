# Generated by Django 2.2.5 on 2020-01-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccion',
            name='anyo',
            field=models.IntegerField(default=2020),
        ),
    ]
