from django.shortcuts import render, redirect
from .models import Amigo, Transitador
from django.http import HttpResponse
from .forms import AmigoForm, TransitadorForm

# Create your views here.

def landing(request):
    return render(request, "myapp/landing.html")

#def landing(request):
    return render(request, "myapp/landing0.html")

# def crear_amigo(request, nombre):
#     if nombre is not None:
#         nuevo_amigo = Amigo(
#             nombre=nombre,
#             fecha_nacimiento_estimada="2024-12-12",
#             especie="Mestizo",
#             descripcion="Enérgico"
#         )
#         nuevo_amigo.save()

#     return render(request, "myapp/crear_amigo.html", {"nombre":nombre})    


def crear_amigo(request):
    if request.method == 'POST':
        form = AmigoForm(request.POST)
        if form.is_valid():
            nuevo_amigo = Amigo(
                nombre=form.cleaned_data['nombre'],
                fecha_nacimiento_estimada=form.cleaned_data['fecha_nacimiento_estimada'],
                especie=form.cleaned_data['especie'],
                descripcion=form.cleaned_data['descripcion'],
                email=form.cleaned_data['email'],

            )
            nuevo_amigo.save()
            #return render(request, "myapp/amigo_creado.html", {"form": form})
            return redirect('gracias')
    else:
        form = AmigoForm()
        return render(request, 'myapp/crear_amigo.html', {'form': form})
    
def crear_transitador(request):
    if request.method == 'POST':
        form = TransitadorForm(request.POST)
        if form.is_valid():
            nuevo_transitador = Transitador(
                nombre=form.cleaned_data['nombre'],
                sobre_mi_hogar=form.cleaned_data['sobre_mi_hogar'],
                email=form.cleaned_data['email'],
            )
            nuevo_transitador.save()
            return redirect('gracias')
    else:
        form = TransitadorForm()
        return render(request, 'myapp/crear_transitador.html', {'form': form})    
    
def gracias(request):
    return render(gracias, "myapp/gracias.html")    


