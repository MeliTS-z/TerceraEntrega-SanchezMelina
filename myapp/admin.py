from django.contrib import admin

# Register your models here.

from .models import Amigo

register_models = [Amigo]

admin.site.register(register_models)