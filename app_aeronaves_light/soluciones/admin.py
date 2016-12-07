# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Solucion



@admin.register(Solucion)
class SolucionAdmin(admin.ModelAdmin):
	list_display   = ('nombre', )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Solucion
