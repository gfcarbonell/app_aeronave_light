# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Pais


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	list_display   = ('nombre', 'codigo_postal', 'imagen', 'descripcion',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Pais
