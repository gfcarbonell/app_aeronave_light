# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Sede

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
	list_display   = ( 'nombre', 'slug' )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Sede
