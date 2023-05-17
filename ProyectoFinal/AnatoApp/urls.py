from django.urls import path
from AnatoApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('registro', views.register, name='Registro'),
    path('login',views.login_request, name="Login"),
    path('errorLogIn',views.usuario, name="ErrorLogIn"),
    path('logout', LogoutView.as_view(template_name='AnatoApp/logout.html'), name = 'Logout'),
    path('ingresarEntrada', views.ingresarEntrada, name='IngresarEntrada'),
    path('verEntradas', views.verEntradas, name='VerEntradas'),
    path('verEntrada/<int:entrada_id>/', views.verEntrada, name='VerEntrada'),
    path('blog', views.blog, name='Blog')
]