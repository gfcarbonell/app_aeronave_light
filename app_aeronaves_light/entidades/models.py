# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify



class Entidad(models.Model):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	nombre 	   						= models.CharField(
									  max_length=255,
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(255),
								  		    ],
									  unique=True, 
									  db_index=True, 
									  help_text='Escribir el nombre de la entidad.')
	slogan 					 		= models.CharField(blank=True, null=True, max_length=255, db_index=True, help_text='Escribir el slogan de la entidad.')
	siglas							= models.CharField(
									  max_length=10, 
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(10),
								  		    ],
									  db_index=True,)
	ruc = models.CharField(
									  verbose_name='R.U.C.', 
									  unique=True, 
									  max_length=20, 
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(20),
								  		    ],
									  db_index=True)
	logotipo  	  					= models.ImageField(blank=True, 
														null=True, 
														upload_to='logotipos_entidades',
														)
	activo 							= models.BooleanField(choices=BOOL_ACTIVO, default=True)
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
		super(Entidad, self).save(*args, **kwargs)

	def get_nombre(self):
		return self.nombre
		
	def get_siglas(self):
		return self.siglas	
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Entidades'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Entidad' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Entidades'#Métodos
