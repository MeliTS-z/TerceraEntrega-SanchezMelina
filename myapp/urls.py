from django.urls import path

#include
from .views import landing, crear_amigo, crear_transitador, gracias, ofrecer_donacion, grdonacion, buscar_amigos, amigo

urlpatterns = [
    path('', landing, name='landing'),
    #path('landing', landing),
    #path('crear-amigo/<str:nombre>/', crear_amigo),
    path('crear-amigo/', crear_amigo, name='crear_amigo'),
    path('crear-transitador/', crear_transitador, name='crear_transitador'),
    path('gracias/', gracias, name='gracias'),
    path('ofrecer-donacion/', ofrecer_donacion, name='ofrecer_donacion'),
    path('gracias-donacion/', grdonacion, name='grdonacion'),
    path('amigos/', amigo, name='amigo'),
    path('amigos/buscar', buscar_amigos, name='buscar_amigos'),

]

#path('admin/', admin.site.urls),

