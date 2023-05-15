from django.shortcuts import render

# Create your views here.
def inicio (request):
    return render (request, 'AnatoApp/inicio.html')


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