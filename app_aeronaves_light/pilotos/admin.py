# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Piloto


@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
	list_display   = ('nombre', )
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Piloto
