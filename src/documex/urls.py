from django.urls import path
#
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("herramienta",views.herramienta, name="herramienta"),
    path("misDocumentos",views.misDocumentos, name="misDocumentos"),
    path("nuevoDocumento",views.nuevoDocumento,name="NuevoDocumento"),
    path("Documentos",views.Documentos, name="Documentos"),
    path("Enviar",views.formEnviar, name="Enviar"),
    path("Enviados",views.misEnvios, name="Enviados"),
    path("formSubir/",views.formSubir, name="formSubir"),
    path("eliminarDoc/<int:id>/",views.eliminarDoc, name="eliminarDoc"),
]
