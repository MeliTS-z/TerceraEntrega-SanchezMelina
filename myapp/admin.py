from django.contrib import admin

# Register your models here.

from .models import Amigo, Transitador, Donacion, SOSrefugio

register_models = [Amigo, Transitador, Donacion, SOSrefugio] 

admin.site.register(register_models)