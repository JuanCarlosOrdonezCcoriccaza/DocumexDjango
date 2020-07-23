from django.db import models

# Create your models here.


class administradores(models.Model):

    username = models.CharField(max_length=50) 
    password = models.CharField(min_length=8)
    email    = models.EmailField(max_length=254)
    img      = models.ImageField(upload_to='pics',null=False)


class usuarios(models.Model):

    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    username     = models.CharField(max_length=50) 
    password     = models.CharField(min_length=8)    
    email        = models.EmailField(max_length=254)
    img          = models.ImageField(upload_to='pics',null=False)
    