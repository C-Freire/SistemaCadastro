from django.contrib import admin

from .models import Ativo, Categoria, CategoriaAtivos

admin.site.register(Ativo)
admin.site.register(Categoria)
admin.site.register(CategoriaAtivos)