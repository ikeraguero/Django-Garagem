from django.contrib import admin

# Register your models here.
from core.models import Marca, Categoria, Carro

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Carro)