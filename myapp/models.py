from django.db import models

# Create your models here.

class Amigo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento_estimada = models.DateField()
    especie = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)


    def __str__(self):
        return f"{self.nombre}"
        


class Transitador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"

