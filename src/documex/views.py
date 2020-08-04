from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def herramienta(request):
    return render(request,"herramienta.html")

def misDocumentos(request):
    return render(request,"herramientas/misDocumentos.html")

def formSubir(request):
    return render(request,"herramientas/formSubir.html")

def nuevoDocumento(request):
    pass
