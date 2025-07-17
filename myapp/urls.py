from django.urls import path

#include
from .views import landing, crear_amigo

urlpatterns = [
    path('', landing, name='landing'),
    #path('landing', landing),
    path('crear-amigo/<str:nombre>/', crear_amigo),
]

#path('admin/', admin.site.urls),

