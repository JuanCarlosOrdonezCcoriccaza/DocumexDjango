from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100)
    dni = models.IntegerField(max_length = 8)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    direccion = models.CharField(max_length=100)
    
    

class Administrador(models.Model):
    id = models.AutoField(primary_key= True)
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100)
    dni = models.IntegerField(max_length = 8)
    password = models.CharField(max_length = 100)
    estado = models.BooleanField(default = False)
    sexo = models.CharField(max_length=1)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    
