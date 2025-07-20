from django.urls import path

#include
from .views import landing, crear_amigo, crear_transitador, gracias

urlpatterns = [
    path('', landing, name='landing'),
    #path('landing', landing),
    #path('crear-amigo/<str:nombre>/', crear_amigo),
    path('crear-amigo/', crear_amigo, name='crear_amigo'),
    path('crear-transitador/', crear_transitador, name='crear_transitador'),
    path('gracias/', gracias, name='gracias'),
]

#path('admin/', admin.site.urls),

