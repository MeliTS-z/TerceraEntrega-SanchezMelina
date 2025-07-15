from django.urls import path

#include
from .views import index

urlpatterns = [
    path('myapp/', index),
]

#path('admin/', admin.site.urls),

