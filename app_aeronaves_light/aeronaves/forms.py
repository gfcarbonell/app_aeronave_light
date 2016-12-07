# -*- encoding: utf-8 -*-
from django import forms
from .models import Aeronave
from django.contrib.admin import widgets


class AeronaveModelForm(forms.ModelForm):
	class Meta:
		model  = Aeronave
		exclude = ['parte_aeronave',
				  'slug',]

		widgets = {
			'parte_aeronave'	    : forms.Select(attrs={'class':'select-field-default'}),
			'tipo_aeronave'	   		: forms.Select(attrs={'class':'select-field-default'}),
			'modelo'	  		    : forms.Select(attrs={'class':'select-field-default'}),
			'marca'	  			    : forms.Select(attrs={'class':'select-field-default'}),
			'color'	  			    : forms.Select(attrs={'class':'select-field-default'}),
			'nombre'				: forms.TextInput(attrs={'class':'input-field-default'}),
			'descripcion' 		    : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'fotografia'    				    : forms.FileInput(attrs={'class':'input-file'}),

			'activo'						: forms.CheckboxInput(attrs={'class':''}),
	      }
