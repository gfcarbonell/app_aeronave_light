# -*- encoding: utf-8 -*-
from django import forms
from .models import CatalogoAeronaveParteAveriaSolucionEmpleado
from django.contrib.admin import widgets


class CatalogoAeronaveParteAveriaSolucionEmpleadoModelForm(forms.ModelForm):
	class Meta:
		model  = CatalogoAeronaveParteAveriaSolucionEmpleado
		fields = '__all__'

		