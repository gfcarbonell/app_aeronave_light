# -*- encoding: utf-8 -*-
from django import forms
from .models import Piloto
from django.contrib.admin import widgets
from betterforms.multiform import MultiModelForm
from usuarios.forms import UsuarioModelForm


class PilotoModelForm(forms.ModelForm):
	class Meta:
		model  = Piloto
		exclude = ['tipo_persona',
				  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
				  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip']

		widgets = {
			'tipo_persona'				   : forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'apellido_paterno'			   : forms.TextInput(attrs={'class':'input-field-default'}),
			'apellido_materno'			   : forms.TextInput(attrs={'class':'input-field-default'}),
			'nombre'					   : forms.TextInput(attrs={'class':'input-field-default'}),
			'descripcion_empleado' 		   : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'observacion_empleado' 		   : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'dni'	   				       : forms.NumberInput(attrs={'class':'select-field-default'}),
			'fecha_nacimiento'				: forms.DateInput(attrs={'class':'date-field-default'}),
			'genero'						: forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'estado_civil'					: forms.Select(attrs={'class':'select-field-default'}),
			'fotografia'    				    : forms.FileInput(attrs={'class':'input-file'}),
			'celular'				: forms.TextInput(attrs={'class':'input-field-default'}),
			'email'				: forms.TextInput(attrs={'class':'input-field-default'}),
		
            'distrito' 		   				: forms.Select(attrs={'class':'select-field-default'}),
			'zona' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'via' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'observacion_direccion'			: forms.Textarea(attrs={'class':'input-field-area-default'}),

			'direccion'						: forms.TextInput(attrs={'class':'input-field-default'}),

			'area'							: forms.Select(attrs={'class':'select-field-default'}),
			'tipo_piloto'					: forms.Select(attrs={'class':'select-field-default'}),
			'cargo'							: forms.Select(attrs={'class':'select-field-default'}),
			'grado_instruccion'				: forms.Select(attrs={'class':'select-field-default'}),
			'profesion'						: forms.Select(attrs={'class':'select-field-default'}),
			'ocupacion'						: forms.Select(attrs={'class':'select-field-default'}),
			'activo'						: forms.CheckboxInput(attrs={'class':''}),
			'apelativo'						: forms.TextInput(attrs={'class':'input-field-default'}),

			'descripcion'					: forms.Textarea(attrs={'class':'input-field-area-default'}),
			'observacion'					: forms.Textarea(attrs={'class':'input-field-area-default'}),

	      }
