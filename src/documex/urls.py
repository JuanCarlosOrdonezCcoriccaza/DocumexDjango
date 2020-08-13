from django.urls import path
#
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("herramienta",views.herramienta, name="herramienta"),
    path("misDocumentos",views.misDocumentos, name="misDocumentos"),
    path("nuevoDocumento",views.nuevoDocumento,name="NuevoDocumento"),
    path("Documentos",views.Documentos, name="Documentos"),
    path("formSubir/",views.formSubir, name="formSubir"),
    path("eliminarDoc/<int:id>/",views.eliminarDoc, name="eliminarDoc"),
]
