from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Usuario
#mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView , UpdateView , DeleteView , TemplateView
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
            messages.info(request,'Credenciales Inválidos:')
            return redirect('login')              
    else:
        return render(request,'loginUser.html')

def loginUser(request):
    
    return render(request,'loginUser.html')

def loginAdmin(request):
    
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
#solo base ejemplo

def logout (request):
    auth.logout(request)
    return redirect('/')

def crearUsuario(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        dni = request.POST['dni']
        username = request.POST['usuario']
        password = request.POST['password']
        fechaNacimiento = request.POST['fnacimiento']
        sexo = request.POST['sexo']
        direccion = request.POST['direccion']
        #controladores
        if('imagen' in request.FILES):
            imagen = request.FILES['imagen']
        else:
            imagem = 'null'
            print("No hay archivo") 

        takemail:bool
        takeuser:bool
        if Usuario.objects.filter(correo=correo).exists():        
            messages.info(request,'Esta direccion de Email ya existe.')
            takemail=False
        else:
            takemail=True
        if Usuario.objects.filter(username=username).exists():
            messages.info(request,'Este usuario ya esta en uso.')
            takeuser=False
        else:
            takeuser=True

        if  takemail and takeuser:
            if 'imagen' in request.FILES:
                usuario=Usuario.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                correo=correo,
                dni=dni,
                username=username,
                password=password,
                fechaNacimiento=fechaNacimiento,
                sexo=sexo,
                direccion=direccion,
                estado=True,
                admin=False,
                imagen=imagen)
            else:
                usuario=Usuario.objects.create(
                nombres=nombres,
                apellidos=apellidos,
                correo=correo,
                dni=dni,
                username=username,
                password=password,
                fechaNacimiento=fechaNacimiento,
                sexo=sexo,
                direccion=direccion,
                estado=True,
                admin=False)
            usuario.set_password(password)    
            usuario.save()    
            messages.info(request,'Usuario creado exitosamente')
            return redirect('loginUser')
        else:
            messages.info(request,'No se puedo Guardar')
            return redirect('registerUser')    
        
    else:
        print("no se envio nada")     
    return render(request,'registerUser.html')

def editarUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    if(request.method == 'GET'):
        print("entro get")
        print(usuario.nombres)
        return render(request,'editarUser.html',{'usuario':usuario})
    elif(request.method == 'POST'):
        print("entro post")

        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        dni = request.POST['dni']
        usuariom = request.POST['usuario']
        password = request.POST['password']
        fechaNacimiento = request.POST['fnacimiento']
        sexo = request.POST['sexo']
        direccion = request.POST['direccion']

        if('imagen' in request.FILES):
            imagen = request.FILES['imagen']
            print(request.FILES['imagen'])
            usuario.imagen=imagen
        else:
            print("No hay archivo")        
        usuario.nombres=nombres
        usuario.apellidos=apellidos
        usuario.correo=correo
        usuario.dni=dni
        usuario.usuario=usuariom
        usuario.set_password(password)
        usuario.fechaNacimiento=fechaNacimiento
        usuario.sexo=sexo
        usuario.direccion=direccion
        usuario.save()
        
        return redirect('listarUser')
    return render(request,'editarUser.html',{'usuario':usuario}) 

def eliminarUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('herramienta')  

def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    contexto ={
        'usuarios' : usuarios
    }
    return render(request,'listarUsers.html',contexto)       

def loginUsuario(request):
    usuario = Usuario.objects.all()
    contexto = {
        "username" : usuario.username,
        "password" : usuario.password
    }
    return render(request,'loginUser.html',contexto)


def loginAdministrador(request):

    administrador = Administrador.objects.all()
    contexto = {
        "usuario" : administrador.usuario,
        "password" : administrador.password
    }    
    return render(request,'loginAdmin.html',contexto)

def crearAdministrador(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        correo = request.POST['correo']
        dni = request.POST['dni']
        username = request.POST['usuario']
        password = request.POST['password']
        fechaNacimiento = request.POST['fnacimiento']
        sexo = request.POST['sexo']
        direccion = request.POST['direccion']
        #controladores
        if('imagen' in request.FILES):
            imagen = request.FILES['imagen']
        else:
            print("No hay archivo") 

        takemail:bool
        takeuser:bool
        if Usuario.objects.filter(correo=correo).exists():        
            messages.info(request,'Esta direccion de Email ya existe.')
            takemail=False
        else:
            takemail=True
        if Usuario.objects.filter(username=username).exists():
            messages.info(request,'Este usuario ya esta en uso.')
            takeuser=False
        else:
            takeuser=True

        if  takemail and takeuser:
            if 'imagen' in request.FILES:
                usuario=Usuario.objects.create(
                    nombres=nombres,
                    apellidos=apellidos,
                    correo=correo,
                    dni=dni,
                    username=username,
                    password=password,
                    fechaNacimiento=fechaNacimiento,
                    sexo=sexo,
                    direccion=direccion,
                    estado=True,
                    admin=True,
                    imagen=imagen)
            else:
                usuario=Usuario.objects.create(
                    nombres=nombres,
                    apellidos=apellidos,
                    correo=correo,
                    dni=dni,
                    username=username,
                    password=password,
                    fechaNacimiento=fechaNacimiento,
                    sexo=sexo,
                    direccion=direccion,
                    estado=True,
                    admin=True)
            usuario.set_password(password)             
            usuario.save()    
            messages.info(request,'Administrador creado exitosamente')
            return redirect('loginAdmin')
        else:
            messages.info(request,'No se puedo Guardar')
            return redirect('registerAdmin')    
        
    else:
        print("no se envio nada")     
    return render(request,'registerAdmin.html')
