from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Detento, Atividade

from django.contrib import admin

# Altera o título da página e o cabeçalho
admin.site.site_header = "Sistema de Remição de Pena"
admin.site.site_title = "Administração - Remição"
admin.site.index_title = "Painel de Controle"


@admin.register(Detento)
class DetentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "processo", "pena_total_dias", "data_inicio")

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ("detento", "tipo", "quantidade", "data_registro")
    list_filter = ("tipo",)
