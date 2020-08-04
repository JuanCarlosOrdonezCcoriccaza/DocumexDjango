from django.urls import path
from . import views

urlpatterns = [
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),
    path("loginAdmin",views.loginAdmin,name="loginAdmin"),
    path("logout",views.logout,name='logout'),
    path("registerUser",views.crearUsuario,name="registerUser")
]
