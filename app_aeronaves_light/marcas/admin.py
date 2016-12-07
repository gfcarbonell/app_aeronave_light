# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Marca


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
	list_display   = ('nombre', )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Marca
