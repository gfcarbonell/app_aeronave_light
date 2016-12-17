# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from aeronaves.models import Aeronave
from tripulaciones.models import Tripulacion
from pilotos.models import Piloto
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class AsignacionTripulacionPiloto(models.Model):
	tripulacion 						= models.ForeignKey(Tripulacion)
	piloto 		   					    = models.ForeignKey(Piloto)
	
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()
		
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre())
		else:
			slug = slugify(self.get_nombre())
			if self.slug != slug:
				self.slug = slug
		super(AsignacionTripulacionPiloto, self).save(*args, **kwargs)

	def get_nombre(self):
		return ' %s | %s ' %(self.tripulacion.get_nombre() , self.piloto.get_nombre_completo())

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Asignaciones_Tripulaciones_Pilotos'
		#Ordenar los registros por un campo especifico
		#ordering = ('orden_aeronave','orden_parte_aeronave', )
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Asignacion Tripulacion Piloto'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Asignaciones Tripulaciones Pilotos'

