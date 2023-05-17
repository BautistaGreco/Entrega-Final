from django.shortcuts import render, redirect


# Create your views here.
def inicio (request):
    return render (request, 'AnatoApp/inicio.html')
def usuario (request):
    return render (request, 'AnatoApp/usuario.html')


#from AnatoApp.forms import UserRegisterForm
#def register(request):
#      if request.method == 'POST':
#            #form = UserCreationForm(request.POST)
#            form = UserRegisterForm(request.POST)
#            if form.is_valid():
#                  username = form.cleaned_data['username']
#                  form.save()
#                  return render(request,"AnatoApp/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
#      else:
#            #form = UserCreationForm()       
#            form = UserRegisterForm()     
#      return render(request,"AnatoApp/registro.html" ,  {"form":form})


from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate




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

from .forms import AlumnoForm

def registro(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"AnatoApp/inicio.html") 
    else:
        form = AlumnoForm()
    
    return render(request,'AnatoApp/register.html', {"form":form})


from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate


class CustomLoginView(LoginView):
    template_name = 'AnatoApp/login.html'  
    authentication_form = AuthenticationForm  
    redirect_authenticated_user = True 