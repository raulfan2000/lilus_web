# Generated by Django 2.2.5 on 2020-01-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='nombre',
            field=models.CharField(default='00000', max_length=32),
        ),
    ]
