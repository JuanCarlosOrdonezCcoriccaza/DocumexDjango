from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#


urlpatterns = [
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),
    path("loginUser",views.loginUser, name="loginUser"),#test
    path("loginAdmin",views.loginAdmin,name="loginAdmin"),
    path("logout",views.logout,name='logout'),
    path("registerUser",views.crearUsuario,name="registerUser"),
    path("listarUsers",views.listarUsuarios,name="listarUsers"),
    path("editarUser/<int:id>/",views.editarUsuario,name="editarUser"),
    path("eliminarUser/<int:id>/",views.eliminarUsuario,name="eliminarUser"),
    path("registerAdmin",views.crearAdministrador,name="registerAdmin") 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)