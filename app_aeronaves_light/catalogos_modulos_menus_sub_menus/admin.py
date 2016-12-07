# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import CatalogoModuloMenuSubMenu 



@admin.register(CatalogoModuloMenuSubMenu)
class CatalogoModuloMenuSubMenuAdmin(admin.ModelAdmin):
	list_display   = ('get_nombre', 'grupo_modulo', 'modulo', 'menu', 'orden_modulo', 'orden_menu', 'imagen', 'url', 'activo', 
					  )
	list_instances = True
	search_fields  = ('nombre',)
	
