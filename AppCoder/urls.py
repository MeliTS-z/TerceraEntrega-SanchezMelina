from django.urls import path
from .views import lista_estudiantes, detalle_estudiante

urlpatterns = [
    path('amigos/', lista_amigos, name='lista_amigos'),
    path('amigos/<int:pk>/', detalle_amigo, name='detalle_amigo'),
]