# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Aeronave



@admin.register(Aeronave)
class AeronaveAdmin(admin.ModelAdmin):
	list_display   = ('get_nombre',)
	list_instances = True
	search_fields  = ('get_nombre',)

	class Meta:
		model = Aeronave
