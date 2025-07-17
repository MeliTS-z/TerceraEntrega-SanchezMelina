from django.shortcuts import render
from .models import Amigo
from django.http import HttpResponse

# Create your views here.

def landing(request):
    return render(request, "myapp/landing.html")

#def landing(request):
    return render(request, "myapp/landing0.html")

def crear_amigo(request, nombre):
    if nombre is not None:
        nuevo_amigo = Amigo(
            nombre=nombre,
            fecha_nacimiento_estimada="2024-12-12",
            especie="Mestizo",
            descripcion="Enérgico"
        )
        nuevo_amigo.save()

    return render(request, "myapp/crear_amigo.html", {"nombre":nombre})    

