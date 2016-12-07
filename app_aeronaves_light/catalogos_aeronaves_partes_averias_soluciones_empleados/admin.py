# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import CatalogoAeronaveParteAveriaSolucionEmpleado


@admin.register(CatalogoAeronaveParteAveriaSolucionEmpleado)
class CatalogoAeronaveParteAveriaSolucionEmpleadoAdmin(admin.ModelAdmin):
	list_display   = ('get_nombre',)
	list_instances = True
	search_fields  = ('nombre',)
