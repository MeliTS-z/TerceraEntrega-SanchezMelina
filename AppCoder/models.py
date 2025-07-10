from django.db import models

# Create your models here.

class Amigo(models.Model):
    nombre = models.CharField(label="Nombre", max_length=100)
    descripcion = models.CharField(widget=models.Textarea, required=False)
    edad = models.IntegerField(min_value=0)
    especie = models.CharField(widget=models.Textarea, required=False)

    def __str__(self):
        return f"{self.nombre}"
        


class Tutor(models.model):
    nombre = models.CharField(label="Nombre", max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"