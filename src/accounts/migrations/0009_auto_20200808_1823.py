# Generated by Django 3.0.8 on 2020-08-08 23:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200808_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fechaNacimiento',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 8, 18, 23, 55, 64946)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(default='M', max_length=1),
        ),
    ]
