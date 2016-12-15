# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import OrdenVuelo


@admin.register(OrdenVuelo)
class OrdenVueloAdmin(admin.ModelAdmin):
	list_display   = ('get_nombre',)
	list_instances = True
	search_fields  = ('nombre',)
	class Meta:
		model = OrdenVuelo
