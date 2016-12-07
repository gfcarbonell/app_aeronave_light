# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import CatalogoAeronaveParteAveriaEmpleado


@admin.register(CatalogoAeronaveParteAveriaEmpleado)
class CatalogoAeronaveParteAveriaEmpleadoAdmin(admin.ModelAdmin):
	list_display   = ('get_nombre',)
	list_instances = True
	search_fields  = ('nombre',)
