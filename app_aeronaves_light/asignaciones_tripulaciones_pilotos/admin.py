# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import AsignacionTripulacionPiloto



@admin.register(AsignacionTripulacionPiloto)
class AsignacionTripulacionPilotoAdmin(admin.ModelAdmin):
	list_display   = ('get_nombre', )
	list_instances = True
	search_fields  = ('nombre',)
