from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Usuario, Administrador
# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['usuario']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Credenciales Inválidos')
            return redirect('loginUsuario')              
    else:
        return render(request,'loginUser.html')

def loginUser(request):
    if request.method=='POST':
        usuario  = request.POST['usuario']
        password = request.POST['password']
        if Usuario.objects.authenticate(usuario=usuario,password=password)
        
            if user is not None:
                Usuario.objects.login(request,user)
                return redirect("/")
            else:
                messages.info(request,'Credenciales Inválidos')
                return redirect('loginUser')              
    else:
        return render(request,'loginUser.html')


def loginAdmin(request):
    if request.method=='POST':
        username = request.POST['usuario']
        password = request.POST['password']
        credenciales = request.POST['credenciales']
        if credenciales == password :
            #mi no entender el error reparalo
            usuario = accounts.authenticate(usuario=username,password=password)
            if usuario is not None:
                accounts.login(request,user)
                return redirect("/")
            else:
                messages.info(request,'Datos no Inválidos')
                return redirect('loginAdministrador')
        else:
            messages.info(request,'Credencial Inválidos')
            return redirect('loginAdministrador')
    else:
        return render(request,'loginAdmin.html')
#este register solo esta de ejemplo no se le esta dando uso aparente
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordC = request.POST['passwordC'] 

        if passwordC == password:   
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                print('Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():        
                messages.info(request,'Email taken')
                print('Email taken')
                return redirect('register')
            else:    
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                messages.info(request,'User Created')
                print('User Created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching...')
            print('Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout (request):
    auth.logout(request)
    return redirect('/')

def crearUsuario(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        dni = request.POST['dni']
        usuario = request.POST['usuario']
        password = request.POST['password']
        fechaNacimiento = request.POST['fnacimiento']
        sexo = request.POST['sexo']
        direccion = request.POST['direccion']
        imagen = request.FILES['imagen']
        #controladores
        takemail:bool
        takeuser:bool
        takevacio:bool
        if nombres=='' or apellidos=='' or correo=='' or dni=='':
            messages.info(request,'Usuario no Creado.')
            return redirect('registerUser')
        else: 
            if usuario=='' or password=='':
                messages.info(request,'Debes crear un Usuario y una Contraseña.')
                takevacio=False
            else:
                takevacio=True
            if Usuario.objects.filter(correo=correo).exists():        
                messages.info(request,'Esta direccion de Email ya existe.')
                takemail=False
            else:
                takemail=True
            if Usuario.objects.filter(usuario=usuario).exists():
                messages.info(request,'Este usuario ya esta en uso.')
                takeuser=False
            else:
                takeuser=True

            if  takemail and takevacio and takeuser:
                if fechaNacimiento=='' or direccion=='' or sexo=='':
                    usuario=Usuario.objects.create(nombres=nombres,apellidos=apellidos,correo=correo,dni=dni,usuario=usuario,password=password,fechaNacimiento=null,sexo=null,direccion=null,estado=True,imagen=imagen)
                else:    
                    usuario=Usuario.objects.create(
                        nombres=nombres,
                        apellidos=apellidos,
                        correo=correo,dni=dni,
                        usuario=usuario,
                        password=password,
                        fechaNacimiento=fechaNacimiento,
                        sexo=sexo,
                        direccion=direccion,
                        estado=True,
                        imagen=imagen)
                usuario.save()
                messages.info(request,'Usuario creado exitosamente')
                print('Usuario Creado con exito')
                return redirect('loginUsuario')
            else:
                return redirect('registerUser')    
            
    else:
        print("no se envio nada")
    return render(request,'registerUser.html')

def editarUsuario(request,id):
    pass
    #usuario = Usuario.objects.get(id = id)
    #if request.method == 'GET':
        
def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    contexto ={
        'usuarios' : usuarios
    }
    return render(request,'listarUsers.html',contexto)       

def loginUsuario(request):
    usuario = Usuario.objects.all()
    contexto = {
        "user" : usuario.nombre,
        "password" : usuario.password
    }
    return render(request,'loginUser.html',contexto)



def crearAdministrador(request):
    #template para registrar administrar
    return render(request,'registerAdmin.html')


def loginAdministrador(request):

    administrador = Administrador.objects.all()
    contexto = {
        "usuario" : administrador.usuario,
        "password" : administrador.password
    }    
    return render(request,'loginAdmin.html',contexto)
