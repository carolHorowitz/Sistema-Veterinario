from django.contrib import admin
from .models import Dados, Prontuario, Usuario

admin.site.register(Dados)
admin.site.register(Prontuario)


@admin.register(Usuario)
class UsuarioAdmin (admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')
