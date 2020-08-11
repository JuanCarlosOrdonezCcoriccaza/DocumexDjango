from django.db import models
from django.contrib.auth.models import User
from accounts.models import Usuario
# Create your models here.
class Documento (models.Model):
    id           = models.AutoField(primary_key = True)
    autor        = models.ForeignKey(Usuario,on_delete=models.CASCADE)  
    archivo      = models.FileField(upload_to="Archivos",null=False)
    titulo       = models.CharField(max_length=100)
    descripcion  = models.TextField(max_length=150)
    estado       = models.BooleanField(default=True)
    enviado      = models.BooleanField(default=False)     
    recibido     = models.BooleanField(default=False)
    costo        = models.FloatField(default=9.9)

    class Meta:
        verbose_name='Documento'
        verbose_name_plural='Documentos'
        ordering=['id']
    def __str__(self):
        return self.id