from django.shortcuts import render


# Create your views here.
def inicio (request):
    return render (request, 'AnatoApp/inicio.html')
def usuario (request):
    return render (request, 'AnatoApp/usuario.html')


from AnatoApp.forms import UserRegisterForm
def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AnatoApp/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"AnatoApp/registro.html" ,  {"form":form})


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
    return render(request, "AnatoApp/login.html", {"form": form})