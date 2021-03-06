# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import SubMenu 



@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = SubMenu
