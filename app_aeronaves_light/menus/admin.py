# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Menu 



@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Menu
