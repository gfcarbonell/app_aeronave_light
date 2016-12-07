# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Empleado 


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
	list_display   = ('get_nombre_completo', 'usuario', 'area', 'tipo_empleado', 'cargo', )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Empleado
