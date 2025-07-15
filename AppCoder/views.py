from django.shortcuts import render
from .models import Amigo, Tutor

#1 get_object_or_404

# Create your views here.

def lista_amigos(request):
    amigos = Amigo.objects.all()
    return render(request, 'AppCoder/amigos_list.html', {'amigos': amigos})

def detalle_amigo(request, pk):
    amigo = get_object_or_404(Amigo, pk=pk)
    return render(request, 'AppCoder/amigo_detail.html', {'amigo': amigo})