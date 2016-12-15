# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import TipoVuelo



@admin.register(TipoVuelo)
class TipoVueloAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = TipoVuelo
