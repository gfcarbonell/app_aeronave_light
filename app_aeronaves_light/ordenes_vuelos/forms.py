# -*- encoding: utf-8 -*-
from django import forms
from .models import OrdenVuelo
from django.contrib.admin import widgets


class OrdenVueloModelForm(forms.ModelForm):
	class Meta:
		model  = OrdenVuelo
		fields = '__all__'
		widgets = {
			'tripulacion'	    		: forms.Select(attrs={'class':'select-field-default'}),
			'aeronave'	   				: forms.Select(attrs={'class':'select-field-default'}),
			'tipo_vuelo'	  		    : forms.RadioSelect(attrs={'class':''}),
			'zona_vuelo'	  			: forms.Select(attrs={'class':'select-field-default'}),
			'turno'	  			   		: forms.Select(attrs={'class':'select-field-default'}),
			'mision'					: forms.TextInput(attrs={'class':'input-field-default'}),
			'altura'					: forms.NumberInput(attrs={'class':'input-field-default'}),
			'galon'						: forms.NumberInput(attrs={'class':'input-field-default'}),
			'fecha_vuelo'				: forms.DateTimeInput(attrs={'class':'input-field-default'})
	      }
