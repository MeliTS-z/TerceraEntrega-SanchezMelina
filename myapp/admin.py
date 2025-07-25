from django.contrib import admin

# Register your models here.

from .models import Amigo, Transitador, Donacion

register_models = [Amigo, Transitador, Donacion] 

admin.site.register(register_models)