# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import ParteAeronave


@admin.register(ParteAeronave)
class ParteAeronaveAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = ParteAeronave
