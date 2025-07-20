from django.contrib import admin

# Register your models here.

from .models import Amigo, Transitador

register_models = [Amigo, Transitador] 

admin.site.register(register_models)