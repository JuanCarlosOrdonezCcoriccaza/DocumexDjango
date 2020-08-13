from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Documento
from accounts.models import Usuario
# Create your views here.
def index(request):
    return render(request,"index.html")
    
def herramienta(request):
    
    return render(request,"herramienta.html")

def misDocumentos(request):
    docs = Documento.objects.all()
    return render(request,"herramientas/misDocumentos.html",{'docs':docs})

def Documentos(request,id):
    usuario = Usuario.objects.get(id=id)
    docs = Documento.objects.all()
    return render(request,"herramientas/Documentos.html",{'docs':docs})

def nuevoDocumento(request):
    print("probando el login_request")
    return render(request,"nuevoDocumento.html")
    

def formSubir(request):
    #usuario = Usuario.objects.get(id=id)
    if request.method=='POST':
        archivo=request.FILES['archivo']
        titulo=request.POST['titulo']
        descripcion=request.POST['descripcion']
        autor=request.user
        #Usuario.username
        documento = Documento.objects.create(autor=autor,archivo=archivo,titulo=titulo,descripcion=descripcion)
        documento.save()
        print("archivo ",archivo)
        print("titulo",titulo)
        print("descripcion",descripcion)
        print("usuario",request.user)
        print("guardado")
        messages.info(request,'Documento guardado')
        return redirect('herramienta')
    else:
        return render(request,'herramientas/formSubir.html')
      

