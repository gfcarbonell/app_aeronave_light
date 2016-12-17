# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


from sedes.models import Sede
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator
from django.template.defaultfilters import slugify


class Area(models.Model):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	sede 							= models.ForeignKey(Sede)
	area_dependiente				= models.ForeignKey('self', related_name='areas_areas_dependientes_related', null=True, blank=True, default=None)
	nombre 	   						= models.CharField(
												  max_length=255,
											      validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		    ],
												  unique=True,
												  db_index=True,
												  help_text='Escribir el nombre del área.')
	siglas							= models.CharField(
									  max_length=10,
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(10),
								  		    ],
									  db_index=True,)
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
		return '%s | %s' %(self.sede.get_nombre_full(), self.get_nombre())

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre())
		else:
			slug = slugify(self.get_nombre())
			if self.slug != slug:
				self.slug = slug
		super(Area, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Areas'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Area'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Areas'#Métodos
