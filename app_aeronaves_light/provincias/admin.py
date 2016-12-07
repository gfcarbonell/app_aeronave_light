# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Provincia


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
	list_display   = ('departamento', 'nombre', 'imagen', 'descripcion',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Provincia
