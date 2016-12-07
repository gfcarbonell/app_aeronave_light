# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Entidad



@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
	list_display   = (
					  'nombre','siglas', )
	
	list_instances = True
	search_fields  = ('nombre', 'numero_documento_identificacion')

	class Meta:
		model = Entidad