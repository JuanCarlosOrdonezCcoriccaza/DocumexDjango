# Generated by Django 3.0.8 on 2020-08-06 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documex', '0002_auto_20200805_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ['id'], 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
    ]