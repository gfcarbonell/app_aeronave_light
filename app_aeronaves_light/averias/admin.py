# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Averia


@admin.register(Averia)
class AveriaAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Averia
