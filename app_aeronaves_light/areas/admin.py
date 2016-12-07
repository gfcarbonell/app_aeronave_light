# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Area
