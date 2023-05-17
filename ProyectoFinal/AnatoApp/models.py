from django.db import models
from django.conf import settings


#####FALTA MAKEMIGRATIONS



# Create your models here.
from django.contrib.auth.models import AbstractUser

class Alumno(AbstractUser):
    password = models.CharField(max_length=128, default='valor_predeterminado')
    username = models.CharField(max_length=150, unique=True, default='asd')
    def __str__(self):
        return f"Nombre: {self.nombre} - Comision {self.comision}"
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    email = models.EmailField()
    

class Profesor(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}"
    nombre = models.CharField(max_length=40)
    email = models.EmailField() 
    clases = models.CharField(max_length=40) 

class Asistencias(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - Comision {self.comision} - Clase {self.clase}"
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    clase = models.CharField(max_length=40)
    presente = models.BooleanField()


from django.contrib.auth.models import User

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha = models.DateField(auto_now_add=True) 
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  