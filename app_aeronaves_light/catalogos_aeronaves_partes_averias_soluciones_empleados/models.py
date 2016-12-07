# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from averias.models import Averia
from empleados.models import Empleado
from soluciones.models import Solucion
from catalogos_aeronaves_partes_averias_soluciones.models import CatalogoAeronaveParteAveriaSolucion

from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class CatalogoAeronaveParteAveriaSolucionEmpleado(models.Model):
	BOOL_ACTIVO 		 						  = ((True, 'Si'), (False, 'No'))
	empleado 				   	    			  = models.ForeignKey(Empleado)
	catalogos_aeronaves_partes_averias_soluciones = models.ForeignKey(CatalogoAeronaveParteAveriaSolucion)
	selecionar 						 			  = models.BooleanField(choices=BOOL_ACTIVO, default=True)
	slug                       					  = models.SlugField(editable=False, max_length=255 , unique=True, db_index=True)

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()

	#Python 2.X
	#def __unicode__(self):
	# return self.nombre

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre())
		else:
			slug = slugify(self.get_nombre())
			if self.slug != slug:
				self.slug = slug
				super(CatalogoAeronaveParteAveriaSolucionEmpleado, self).save(*args, **kwargs)

	def get_nombre(self):
		return ' %s | %s ' %(self.catalogos_aeronaves_partes_averias_soluciones.get_nombre() , self.empleado.get_nombre_completo())

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Catalogos_Aeronaves_Partes_Averias_Soluciones_Empleados'
		#Ordenar los registros por un campo especifico
		#ordering = ('orden_aeronave','orden_parte_aeronave', )
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Catalogo Aeronave Parte Averia Solucion Empleado'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Catalogos Aeronaves Partes Averias Soluciones Empleados'
