from django.db import models
from datetime import date,datetime
#from django.utils.timezone.now import date,datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self,correo,username,nombres,apellidos,dni,password=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electronico')
        usuario = self.model(
            username=username
            ,correo=self.normalize_email(correo)
            ,nombres=nombres
            ,apellidos=apellidos
            ,dni=dni
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    """
    def create_superuser(self,username,correo,nombres,apellidos,dni,password):
        usuario = self.create_user(
            correo
            ,username=username
            ,nombres=nombres
            ,apellidos=apellidos
            ,dni=dni
            ,password=password
        )
        usuario.admin = True
        usuario.save()
        return usuario
    """
class Usuario(AbstractBaseUser):
    id          = models.AutoField(primary_key = True)
    username     = models.CharField('Nombre de Usuario',unique=True, max_length=100)
    correo      = models.EmailField('Correo Electronico',unique=True,max_length=100)
    nombres     = models.CharField(max_length = 100)
    apellidos   = models.CharField(max_length = 100)
    dni         = models.IntegerField('DNI del Usuario',unique=True,blank=False)
    password    = models.CharField(max_length = 100)
    fechaNacimiento = models.DateField(default=date.today(),blank=True,null=False)
    sexo        = models.CharField(max_length=1,default='M',null=False)
    direccion   = models.CharField(max_length=100,blank=True,null=True)
    estado      = models.BooleanField(default=True)
    admin       = models.BooleanField(default=False)
    imagen      = models.ImageField(upload_to="foto-Usuario",blank=True,null=True)
    #is_active   = models.BooleanField(default=False)
    #is_staff    = models.BooleanField(default=False)
    objects     = UsuarioManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['correo','nombres','apellidos','dni']

    def __str__(self):
        return f'Usuario{self.username}'
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.admin
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'

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

class AdministradorManager(BaseUserManager):
    def create_superuser(self,correo,username,nombres,apellidos,password):
        if not correo:
            raise ValueError('El administrador debe tener un correo electronico')
        administrador = self.model(
            username=username
            ,correo=self.normalize_email(correo)
            ,nombres=nombres
            ,apellidos=apellidos
            ,dni=dni
            ,clave=nombres[0:1]+apellidos[0:1]+(str)(dni)
        )
        print("Tu clave es:"+clave)
        administrador.set_password(password)
        administrador.save()
        return usuario    

class Administrador(AbstractBaseUser):
    id          = models.AutoField(primary_key = True)
    username     = models.CharField('Nombre de Usuario',unique=True, max_length=100)
    correo      = models.EmailField('Correo Electronico',unique=True,max_length=100)
    nombres     = models.CharField(max_length = 100)
    apellidos   = models.CharField(max_length = 100)
    dni         = models.IntegerField('DNI del Usuario',unique=True,blank=False)
    clave       = models.CharField(max_length = 100)
    password    = models.CharField(max_length = 100)
    fechaNacimiento = models.DateField(default=date.today(),blank=True,null=False)
    sexo        = models.CharField(max_length=1,default='M',null=False)
    direccion   = models.CharField(max_length=100,blank=True,null=True)
    estado      = models.BooleanField(default=True)
    admin       = models.BooleanField(default=True)
    imagen      = models.ImageField(upload_to="foto-Usuario",blank=True,null=True)
    objects     = AdministradorManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['correo','nombres','apellidos','dni','clave']

    def __str__(self):
        return f'Usuario{self.username}'
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.admin
    class Meta:
        verbose_name='Administrador'
        verbose_name_plural='Administradores'
    #def __str__(self):
    #    return self.usuario
