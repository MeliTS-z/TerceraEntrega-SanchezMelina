from django.urls import path

#include
from .views import landing, crear_amigo

urlpatterns = [
    path('myapp/landing', landing),
    path('myapp/crear-amigo/<str:nombre>/', crear_amigo),
]

#path('admin/', admin.site.urls),

