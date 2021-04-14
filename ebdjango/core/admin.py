from django.contrib import admin

from core import models as mod_core


@admin.register(mod_core.Market)
class MarketAdmin(admin.ModelAdmin):
    pass


@admin.register(mod_core.RateGen)
class RateGenAdmin(admin.ModelAdmin):
    list_display = [
        'pk_control',
        'id_historico_tasas_gen',
        'tasa',
        'nodo',
        'curva',
        'expectativa',
        'precio',
        'duracion',
    ]
