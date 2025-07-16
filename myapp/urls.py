from django.urls import path

#include
from .views import landing

urlpatterns = [
    path('myapp/', landing),
]

#path('admin/', admin.site.urls),

