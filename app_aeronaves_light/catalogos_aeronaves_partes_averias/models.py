# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from aeronaves.models import Aeronave
from partes_aeronaves.models import ParteAeronave
from averias.models import Averia
from soluciones.models import Solucion
from catalogos_aeronaves_partes.models import CatalogoAeronaveParte
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class CatalogoAeronaveParteAveria(models.Model):
	solucion 				   		= models.ManyToManyField(Solucion, through='catalogos_aeronaves_partes_averias_soluciones.CatalogoAeronaveParteAveriaSolucion')
	catalogo_aeronave_parte			= models.ForeignKey(CatalogoAeronaveParte)
	averia 							= models.ForeignKey(Averia)
	descripcion		    			= models.TextField(verbose_name='Descripción', blank=True, null=True, help_text='(Opcional)')
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )

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
		super(CatalogoAeronaveParteAveria, self).save(*args, **kwargs)

	def get_nombre(self):
		return ' %s | %s ' %(self.catalogo_aeronave_parte.get_nombre() , self.averia.get_nombre())

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Catalogos_Aeronaves_Partes_Averias'
		#Ordenar los registros por un campo especifico
		#ordering = ('orden_aeronave','orden_parte_aeronave', )
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Catalogo Aeronave Parte Averia'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Catalogos Aeronaves Partes Averias'
