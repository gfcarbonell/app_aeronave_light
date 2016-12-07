# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Departamento 


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display   = ('pais', 'nombre', 'codigo_postal', 'imagen', 'descripcion')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Departamento
