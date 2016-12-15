# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Tripulacion


@admin.register(Tripulacion)
class TripulacionAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Tripulacion
