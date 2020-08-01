from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Usuario, Administrador
# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')              
    else:
        return render(request,'loginUser.html')


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

        usuario=Usuario.objects.create(nombres=nombres,apellidos=apellidos,correo=correo,dni=dni,usuario=usuario,password=password,fechaNacimiento=fechaNacimiento,sexo=sexo,direccion=direccion)
        usuario.save()
        messages.info(request,'Usuario creado exitosamente')
        print('Usuario Creado con exito')
    else:
        print("no se envio nada")
    return render(request,'registerUser.html')

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
        "user" : administrador.nombre,
        "password" : administrador.password
    }
    return render(request,'loginAdmin.html')