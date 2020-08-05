from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Documento
from accounts.models import Administrador,Usuario
# Create your views here.
def index(request):
    return render(request,"index.html")
    
def herramienta(request):
    return render(request,"herramienta.html")

def misDocumentos(request):
    docs = Documento.objects.all() 
    print(docs)
    return render(request,"herramientas/misDocumentos.html",{'docs':docs})

def nuevoDocumento(request):
    #return render(request,"herramientas/formSubir.html")
    pass

def formSubir(request):
    if request.method=='POST':
        archivo=request.FILES['archivo']
        titulo=request.POST['titulo']
        descripcion=request.POST['descripcion']
        autor=request.user
        documento = Documento.objects.create(autor=autor,archivo=archivo,titulo=titulo,descripcion=descripcion)
        documento.save()
        print("archivo ",archivo)
        print("titulo",titulo)
        print("descripcion",descripcion)
        print("usuario",request.user)
        print("guardado")
        messages.info(request,'Documento guardado')
        #docs=Documento.objects.all()
        return redirect('/')
    else:
        return render(request,'herramientas/formSubir.html')
      

