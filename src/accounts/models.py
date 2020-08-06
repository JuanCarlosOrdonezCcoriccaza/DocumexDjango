from django.db import models

# Create your models here.


#class administradores(models.Model):

#    username = models.CharField(max_length=50) 
#    password = models.CharField(min_length=8)
#    email    = models.EmailField(max_length=254)
#    img      = models.ImageField(upload_to='pics',null=False)


#class usuarios(models.Model):

#    first_name   = models.CharField(max_length=50)
#    last_name    = models.CharField(max_length=50)
#    username     = models.CharField(max_length=50) 
#    password     = models.CharField(min_length=8)    
#    email        = models.EmailField(max_length=254)
#    img          = models.ImageField(upload_to='pics',null=False)
    
class Usuario(models.Model):
    id          = models.AutoField(primary_key = True)
    nombres     = models.CharField(max_length = 100)
    apellidos   = models.CharField(max_length = 100)
    correo      = models.EmailField(max_length = 100)
    dni         = models.IntegerField()
    usuario     = models.CharField(max_length=100)
    password    = models.CharField(max_length = 100)
    fechaNacimiento = models.DateField(null=False)
    sexo        = models.CharField(max_length=1,null=False)
    direccion   = models.CharField(max_length=100,null=False)
    estado      = models.BooleanField(default=False)
    imagen      = models.ImageField(upload_to="foto-Usuario" , null = True)
    def __str__(self):
        return self.usuario
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'

class Administrador(models.Model):
    id          = models.AutoField(primary_key= True)
    nombres     = models.CharField(max_length = 100)
    apellidos   = models.CharField(max_length = 100)
    correo      = models.EmailField(max_length = 100)
    dni         = models.IntegerField()
    usuario     = models.CharField(max_length=100)
    password    = models.CharField(max_length = 100)
    estado      = models.BooleanField(default = False)
    fechaNacimiento = models.DateField()
    sexo        = models.CharField(max_length=1)
    direccion   = models.CharField(max_length=100)
    imagen      = models.ImageField(upload_to="foto-Administrador" , null=True)
    def __str__(self):
        return self.usuario
    class Meta:
        verbose_name='Administrador'
        verbose_name_plural='Administradores'
