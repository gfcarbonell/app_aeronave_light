# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import ZonaVuelo 

@admin.register(ZonaVuelo)
class ZonaVueloAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = ZonaVuelo
