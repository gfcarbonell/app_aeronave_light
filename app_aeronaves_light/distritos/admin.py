# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Distrito 


@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
	list_display   = ('provincia', 'nombre', 'imagen', 'descripcion')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Distrito
