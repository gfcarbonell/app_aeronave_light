# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import TipoEmpleado 


@admin.register(TipoEmpleado)
class TipoEmpleadoAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = TipoEmpleado
