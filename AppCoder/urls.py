from django.urls import path
from .views import lista_amigos, detalle_amigo

urlpatterns = [
    path('amigos/', lista_amigos, name='lista_amigos'),
    path('amigos/<int:pk>/', detalle_amigo, name='detalle_amigo'),
]
