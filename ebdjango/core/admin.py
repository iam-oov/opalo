from django.contrib import admin

from core import models as mod_core


@admin.register(mod_core.Market)
class MarketAdmin(admin.ModelAdmin):
  pass