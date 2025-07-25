from django.db import models

# Create your models here.

class Amigo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento_estimada = models.DateField()
    especie = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)
    email = models.EmailField()


    def __str__(self):
        return self.nombre
        


class Transitador(models.Model):
    nombre = models.CharField(max_length=100)
    sobre_mi_hogar = models.CharField(max_length=2000)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"


class Donacion(models.Model):
    nombre = models.CharField(max_length=100)
    objeto_a_donar = models.CharField(max_length=200)
    punto_de_encuentro = models.CharField(max_length=180)
    dia_hora_preferencia = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"

