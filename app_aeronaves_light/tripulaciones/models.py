# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from pilotos.models import Piloto
from aeronaves.models import Aeronave
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class Tripulacion(models.Model):
	aeronaves 				   		= models.ManyToManyField(Aeronave, through='ordenes_vuelos.OrdenVuelo')
	piloto 							= models.ManyToManyField(Piloto, through='asignaciones_tripulaciones_pilotos.AsignacionTripulacionPiloto')
	nombre 	   						= models.CharField(
											  max_length=100,
										      validators=[
										  		        MinLengthValidator(1),
										  		        MaxLengthValidator(100),
										  		    ],
											  unique=True, 
											  db_index=True, 
											  help_text='Escribir el nombre de la tripulación.')

	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )


	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()
	
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre	

	def get_nombre(self):
		return self.nombre
	
	def get_nombre_full(self):
		return ' %s ' %(self.get_nombre())

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre()) 
		else:
			slug = slugify(self.get_nombre()) 
			if self.slug != slug:
				self.slug = slug
		super(Tripulacion, self).save(*args, **kwargs)
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Tripulaciones'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Tripulacion' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Tripulaciones'


