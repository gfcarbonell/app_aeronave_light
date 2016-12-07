# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import DocumentoIdentificacion 


@admin.register(DocumentoIdentificacion)
class DocumentoIdentificacionAdmin(admin.ModelAdmin):
	list_display   = ('nombre', 'siglas', 'numero_digito',)
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = DocumentoIdentificacion
