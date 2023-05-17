from django.shortcuts import render, redirect


# Create your views here.
def inicio (request):
    return render (request, 'AnatoApp/inicio.html')
def usuario (request):
    return render (request, 'AnatoApp/usuario.html')
def about (request):
    return render (request, 'AnatoApp/about.html')


from AnatoApp.forms import UserRegisterForm
def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AnatoApp/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"AnatoApp/register.html" ,  {"form":form})


from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "AnatoApp/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AnatoApp/errorLogIn.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AnatoApp/errorLogIn.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "AnatoApp/logIn.html", {"form": form})


from AnatoApp.forms import EntradaForm

from django.contrib.auth.decorators import login_required

@login_required
def ingresarEntrada(request):
    if request.method == "POST":
        form = EntradaForm(request.POST)
        print (form)

        if form.is_valid():
            informacion = form.cleaned_data
            entrada = form.save(commit=False)  # Crear una instancia del modelo pero no guardarla todavía
            entrada.autor = request.user  # Asignar el autor actual
            entrada.save()  # Guardar la instancia
            return render(request, 'AnatoApp/inicio.html')
    else:
        form = EntradaForm()
        
    contexto = {"form": form}
    return render(request, "AnatoApp/ingresarEntrada.html", contexto)


from AnatoApp.models import Entrada


def verEntradas(request): #Lista de entrads
    entradas = Entrada.objects.all()
    contexto = {"entradas": entradas}
    return render(request, "AnatoApp/verEntradas.html", contexto)


def verEntrada(request, entrada_id): #Ingresar a una
    entrada = Entrada.objects.get(id=entrada_id)
    contexto = {"entrada": entrada}
    return render(request, "AnatoApp/verEntrada.html", contexto)

def blog (request):
    return render (request, 'AnatoApp/blog.html')

from .forms import UserEditForm

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "AnatoApp/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AnatoApp/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

from .forms import AsistenciasFormulario

@login_required
def asistenciasFormulario(request):
     if request.method == "POST":
          miFormulario = AsistenciasFormulario(request.POST)
          print (miFormulario)
          if miFormulario.is_valid:
               informacion = miFormulario.cleaned_data
               asistencia = Asistencias (nombre = informacion["nombre"], comision = informacion["comision"], clase = informacion["clase"], presente = informacion["presente"])
               asistencia.save()
               return render (request, "AnatoApp/inicio.html")
     else:
          miFormulario = AsistenciasFormulario()
     return render (request,"AnatoApp/asistenciasFormulario.html", {"miFormulario":miFormulario})



def busquedaAsistencia (request):
     return render (request, "AnatoApp/busquedaAsistencia.html")

from .models import Asistencias
from django.http import HttpResponse

def buscar(request):
     if request.GET["nombre"]:
          nombre = request.GET["nombre"]
          asistencias = Asistencias.objects.filter(nombre__icontains=nombre)

          return render (request, "AnatoApp/resultadosBusqueda.html", {"asistencias":asistencias, "nombre":nombre})
     else:
          respuesta = "no enviaste datos"
     return HttpResponse (respuesta)