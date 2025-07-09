from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Estás en el lugar correcto para encontrar a tu amigo de 4 patas"}
    return render(request, "myapp/index.html", context)
