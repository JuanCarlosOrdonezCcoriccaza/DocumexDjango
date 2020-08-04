from django.db import models
from django.contrib.auth.models import User
from accounts.models import Administrador,Usuario
# Create your models here.
class Documento (models.Model):
    id           = models.AutoField(primary_key = True)
    autor        = models.ForeignKey(verbose_name="Usuario")  
    archivo      = models.FileField(upload_to="Archivos",null=False)
    titulo       = models.TextField(max_length=100)
    descripcion  = models.TextField(max_length=150)
    estado       = models.BooleanField(default=True)
    enviado      = models.BooleanField(default=False)     
    recibido     = models.BooleanField(default=False)
    costo        = models.FloatField()
    #ubicacion