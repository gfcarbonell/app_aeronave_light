# -*- encoding: utf-8 -*-
from django import forms
from .models import AsignacionTripulacionPiloto
from django.contrib.admin import widgets


class AsignacionTripulacionPilotoModelForm(forms.ModelForm):
	class Meta:
		model  = AsignacionTripulacionPiloto
		fields = '__all__'
		widgets = {
			'tripulacion'	    		: forms.Select(attrs={'class':'select-field-default'}),
			'piloto'	   				: forms.Select(attrs={'class':'select-field-default'}),

	     }
