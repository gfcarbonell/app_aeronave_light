# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import TipoPiloto



@admin.register(TipoPiloto)
class TipoPilotoAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = TipoPiloto
