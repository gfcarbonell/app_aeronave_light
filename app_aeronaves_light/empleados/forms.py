# -*- encoding: utf-8 -*-
from django import forms
from .models import Empleado
from django.contrib.admin import widgets
from betterforms.multiform import MultiModelForm
from usuarios.forms import UsuarioModelForm


class EmpleadoModelForm(forms.ModelForm):
	class Meta:
		model  = Empleado
		exclude = ['usuario',]

		widgets = {
			'tipo_persona'				   : forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'apellido_paterno'			   : forms.TextInput(attrs={'class':'input-field-default'}),
			'apellido_materno'			   : forms.TextInput(attrs={'class':'input-field-default'}),
			'nombre'					    : forms.TextInput(attrs={'class':'input-field-default'}),
			'descripcion' 		  			: forms.Textarea(attrs={'class':'input-field-area-default'}),
			'observacion' 		  		    : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'dni'	   						: forms.NumberInput(attrs={'class':'input-field-default'}),
			'fecha_nacimiento'				: forms.DateInput(attrs={'class':'date-field-default'}),
			'genero'						: forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'estado_civil'					: forms.Select(attrs={'class':'select-field-default'}),
			'fotografia'    				: forms.FileInput(attrs={'class':'input-file'}),
			'telefono'						 : forms.TextInput(attrs={'class':'input-field-default'}),
			'celular'						 : forms.TextInput(attrs={'class':'input-field-default'}),
			'email'							 : forms.TextInput(attrs={'class':'input-field-default'}),
			'distrito' 		   				: forms.Select(attrs={'class':'select-field-default'}),
			'zona' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'via' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'observacion_zona_via'			: forms.Textarea(attrs={'class':'input-field-area-default'}),
			'celular'				: forms.TextInput(attrs={'class':'input-field-default'}),
			'email'				: forms.TextInput(attrs={'class':'input-field-default'}),
		
			'direccion'						 : forms.TextInput(attrs={'class':'input-field-default'}),
			
			'area'							: forms.Select(attrs={'class':'select-field-default'}),
			'tipo_empleado'					: forms.Select(attrs={'class':'select-field-default'}),
			'cargo'							: forms.Select(attrs={'class':'select-field-default'}),
			'fecha_inicio_contratacion'		: forms.DateInput(attrs={'class':'date-field-default'}),
			'fecha_fin_contratacion'		: forms.DateInput(attrs={'class':'date-field-default'}),
			'fecha_cese'					: forms.DateInput(attrs={'class':'date-field-default'}),
			'activo'						: forms.CheckboxInput(attrs={'class':''}),

	      }


class EmpleadoUsuarioForm(MultiModelForm):
	form_classes = {
        'model_form_empleado': EmpleadoModelForm,
        'model_form_usuario': UsuarioModelForm,
    }
