# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Via 

@admin.register(Via)
class ViaAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Via
