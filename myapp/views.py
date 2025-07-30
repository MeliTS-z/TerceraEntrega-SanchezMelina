from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Amigo, Transitador, Donacion, SOSrefugio
from django.http import HttpResponse
from .forms import AmigoForm, TransitadorForm, DonacionForm, SOSrefugioForm

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

def ofrecer_donacion(request):
    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            nueva_donacion = Donacion(
                nombre=form.cleaned_data['nombre'],
                objeto_a_donar=form.cleaned_data['objeto_a_donar'],
                punto_de_encuentro=form.cleaned_data['punto_de_encuentro'],
                dia_hora_preferencia=form.cleaned_data['dia_hora_preferencia'],
                email=form.cleaned_data['email'],
            )
            nueva_donacion.save()
            return redirect('grdonacion')
    else:
        form = DonacionForm()
        return render(request, 'myapp/ofrecer_donacion.html', {'form': form})    
    
def grdonacion(request):
    return render(grdonacion, "myapp/grdonacion.html")

def aec(request):
    return render(aec, "myapp/ayuda_en_camino.html")

def amigo(request):
    amigo = Amigo.objects.all()
    return render(request, 'myapp/amigos.html', {'amigo': amigo})


def buscar_amigos(request):
        if request.method == 'GET':
            nombre = request.GET.get('nombre', '')
            amigo = Amigo.objects.filter(nombre__icontains=nombre)
            return render(request, 'myapp/amigos.html', {'amigo': amigo, 'nombre': nombre})
        

def transitador(request):
    transitador = Transitador.objects.all()
    return render(request, 'myapp/transitadores.html', {'transitador': transitador}) 


def buscar_transitadores(request):
    if request.method == 'GET':
            nombre = request.GET.get('nombre', '')
            transitador = Transitador.objects.filter(nombre__icontains=nombre)
            return render(request, 'myapp/transitadores.html', {'transitador': transitador, 'nombre': nombre})


class SOSrefugioCreateView (CreateView):
    model = SOSrefugio
    form_class = SOSrefugioForm
    template_name = 'myapp/SOS_refugio.html'
    success_url = reverse_lazy('ayuda_en_camino')

class SOSrefugioDetailView (DetailView):
    model = SOSrefugio
    template_name = 'myapp/detalle_listar_SOS.html'
    context_object_name = 'detallelistaSOS'

class SOSrefugioListView (ListView):
    model = SOSrefugio
    template_name = 'myapp/listar_SOS.html'
    context_object_name = 'listaSOS'

class SOSrefugioUpdateView (UpdateView):
    model = SOSrefugio
    form_class = SOSrefugioForm
    template_name = 'myapp/SOS_refugio.html'
    success_url = reverse_lazy('lista_SOS')

class SOSrefugioDeleteView (DeleteView):
    model = SOSrefugio
    template_name = 'myapp/eliminar_SOS_refugio.html'
    success_url = reverse_lazy('lista_SOS')


