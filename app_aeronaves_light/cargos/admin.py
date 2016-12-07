# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Cargo 


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display   = ('nombre', )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Cargo
