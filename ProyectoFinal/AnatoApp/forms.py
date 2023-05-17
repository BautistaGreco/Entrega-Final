from django import forms
from django.db import models
from .models import Alumno


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from AnatoApp.models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'subtitulo', 'cuerpo']


class AlumnoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Alumno
        fields = ['nombre', 'comision', 'email', 'password']
