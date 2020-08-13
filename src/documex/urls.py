from django.urls import path
#
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("herramienta",views.herramienta, name="herramienta"),
    path("misDocumentos",views.misDocumentos, name="misDocumentos"),
    path("nuevoDocumento",views.nuevoDocumento,name="NuevoDocumento"),
    path("Documentos/<int:id>/",views.Documentos, name="Documentos"),
    path("formSubir/<int:id>/",views.formSubir, name="formSubir"),

]
