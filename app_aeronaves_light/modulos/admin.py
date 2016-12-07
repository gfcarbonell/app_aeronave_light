# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Modulo 



@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Modulo
