from django.db import models

# Create your models here.
class Amigo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=2000)
    edad = models.IntegerField()
    especie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"
        


class Tutor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
