from django.urls import path
from AnatoApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('register', views.register, name='Registro'),
    path('logIn',views.login_request, name="Login"),
    path('errorLogIn',views.usuario, name="ErrorLogIn"),
    path('logout', LogoutView.as_view(template_name='AnatoApp/logout.html'), name = 'Logout'),
    path('ingresarEntrada', views.ingresarEntrada, name='IngresarEntrada'),
    path('verEntradas', views.verEntradas, name='VerEntradas'),
    path('verEntrada/<int:entrada_id>/', views.verEntrada, name='VerEntrada'),
    path('blog', views.blog, name='Blog'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('about', views.about, name='About'),
    path('asistenciasFormulario', views.asistenciasFormulario, name='AsistenciasFormulario'),
    path('busquedaAsistencia', views.busquedaAsistencia, name='BusquedaAsistencia'),
    path('buscar/', views.buscar),
    path('leerAsistencias',views.leerAsistencias,name='LeerAsistencias'),
    path('eliminarAsistencia/<asistencia_nombre>/', views.eliminarAsistencias, name="EliminarAsistencia"),
    path('editarAsistencia/<asistencia_nombre>/', views.editarAsistencia, name="EditarAsistencia"),
]