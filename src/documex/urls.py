from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("herramienta",views.herramienta, name="herramienta"),
    path("misDocumentos",views.misDocumentos, name="misDocumentos"),
    path("formSubir",views.formSubir, name="formSubir"),
    path("nuevoDocumento",views.nuevoDocumento, name="nuevoDocumento"),
]

