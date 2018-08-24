from django.contrib import admin
from . models import Color, Marca, Modelo, AlmacenCarro

# Register your models here.
admin.site.register(Color)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(AlmacenCarro)