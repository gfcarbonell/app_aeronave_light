# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import TipoAeronave



@admin.register(TipoAeronave)
class TipoAeronaveAdmin(admin.ModelAdmin):
	list_display   = ('nombre', )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = TipoAeronave
