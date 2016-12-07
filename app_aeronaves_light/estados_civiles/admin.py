# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import EstadoCivil 


@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
	list_display   = ('nombre', )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = EstadoCivil
