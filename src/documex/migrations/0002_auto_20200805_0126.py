# Generated by Django 3.0.8 on 2020-08-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='costo',
            field=models.FloatField(default=9.9),
        ),
        migrations.AlterField(
            model_name='documento',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
