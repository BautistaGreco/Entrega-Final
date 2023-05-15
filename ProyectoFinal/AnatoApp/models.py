from django.db import models



#####FALTA MAKEMIGRATIONS



# Create your models here.
class Alumno(models.Model):
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

