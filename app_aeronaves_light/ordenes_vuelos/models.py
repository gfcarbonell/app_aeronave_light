# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from aeronaves.models import Aeronave
from tripulaciones.models import Tripulacion
from tipos_vuelos.models import TipoVuelo
from zonas_vuelos.models import ZonaVuelo
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
from datetime import datetime 


class OrdenVuelo(models.Model):
	CHOICES_TURNO 					= 	(('Mañana', 'Mañana'),('Tarde', 'Tarde'),('Noche', 'Noche'))
	tripulacion						= 	models.ForeignKey(Tripulacion)
	aeronave 					    = 	models.ForeignKey(Aeronave)
	
	tipo_vuelo 						= 	models.ForeignKey(TipoVuelo)
	zona_vuelo 						= 	models.ForeignKey(ZonaVuelo)
	turno 	   						= 	models.CharField(
									  	max_length=10,
								      	validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(10),
								  		    ],
 										choices = CHOICES_TURNO
									  )

	mision	   						= 	models.CharField(
									  	max_length=100,
								      	validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(100),
								  		    ],
									  	)
	altura	   						= 	models.PositiveSmallIntegerField(default=0)
	galon	   						= 	models.PositiveSmallIntegerField(default=0)
	fecha_vuelo	   					= 	models.DateTimeField() 
	slug							= 	models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )

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
		super(OrdenVuelo, self).save(*args, **kwargs)

	def get_nombre(self):
		return ' %s | %s | %s | %s' %(self.tripulacion.get_nombre() , self.aeronave.get_nombre(), self.tipo_vuelo, self.mision)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Ordenes_Vuelos'
		#Ordenar los registros por un campo especifico
		#ordering = ('orden_aeronave','orden_parte_aeronave', )
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Orden Vuelo'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Ordenes Vuelos'
