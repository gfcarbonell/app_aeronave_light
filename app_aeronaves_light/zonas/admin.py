# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Zona 

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Zona
