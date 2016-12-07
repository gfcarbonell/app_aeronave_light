from django.contrib import admin

from .models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	list_display   = ('nombre',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Color
