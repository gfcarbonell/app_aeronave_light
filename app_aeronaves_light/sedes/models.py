# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from entidades.models import Entidad
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
from django.core.validators import EmailValidator


class Sede(models.Model):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	entidad 		 				= models.ForeignKey(Entidad)
	nombre 	   						= models.CharField(
												  max_length=255,
											      validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		    ],
												  unique=True,
												  db_index=True,
												  help_text='Escribir el nombre de la sede.')
	activo 							= models.BooleanField(choices=BOOL_ACTIVO, default=True)
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre_full()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre
	def get_nombre(self):
		return self.nombre

	def get_nombre_full(self):
		return ' %s | %s ' %(self.entidad.get_nombre(), self.get_nombre())

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre())
		else:
			slug = slugify(self.get_nombre())
			if self.slug != slug:
				self.slug = slug
		super(Sede, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Sedes'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Sede'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Sedes'
