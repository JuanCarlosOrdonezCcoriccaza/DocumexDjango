from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100)
    dni = models.IntegerField()
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return self.usuario
    

class Administrador(models.Model):
    id = models.AutoField(primary_key= True)
    nombres = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 100)
    dni = models.IntegerField()
    usuario = usuario = models.CharField(max_length=100)
    password = models.CharField(max_length = 100)
    estado = models.BooleanField(default = False)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    direccion = models.CharField(max_length=100)
    
