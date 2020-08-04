from django.db import models

# Create your models here.
class Documento (models.Model):
    id           = models.AutoField(primary_key = True)
    dniautor     = models.IntegerField(models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE))
    archivo      = models.FileField(upload_to="Archivos",null=False)
    titulo       = models.TextField(max_length=100)
    descripcion  = models.TextField(max_length=150)
    estado       = models.BooleanField(default=True)
    enviado      = models.BooleanField(default=False)     
    recibido     = models.BooleanField(default=False)
    costo        = models.FloatField()