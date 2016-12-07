# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from estados_civiles.models import EstadoCivil
from distritos.models import Distrito
from vias.models import Via
from zonas.models import Zona

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify


class Persona(models.Model):
	CHOICES_GENERO 	 				= (('Masculino', 'Masculino'), ('Femenino', 'Femenino'))

	apellido_paterno 		 		= models.CharField(max_length=255,
													   help_text='Escribir apellido paterno.',
													   validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
													   db_index=True)
	apellido_materno 		 		= models.CharField( max_length=255,
														validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
														help_text='Escribir apellido materno.',
														db_index=True)
	nombre 			 		 		= models.CharField( verbose_name='Nombre(s)',
													    max_length=255,
														validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
													    help_text='Escribir nombre(s).',
													    db_index=True)
	dni = models.CharField(verbose_name='D.N.I.',
													   unique=True,
													   max_length=8,
													   validators=[
													   	        MinLengthValidator(1),
													   	        MaxLengthValidator(8),
													   	    ],
													   help_text='Escribir número documento identificación.',
													   db_index=True)
	fecha_nacimiento			    = models.DateField()
	genero 							= models.CharField(verbose_name='Género', choices=CHOICES_GENERO, default=CHOICES_GENERO[0][1], max_length=9)
	estado_civil 					= models.ForeignKey(EstadoCivil, default=1, related_name='%(app_label)s_%(class)s_related')
	telefono 						= models.CharField(verbose_name="Télefono",
													    max_length=20,
													    blank=True, null=True, help_text='(Opcional).')
	celular 						= models.CharField(verbose_name="Celular",
														max_length=20, blank=True, null=True, help_text='(Opcional).')
	email 							= models.EmailField(
														verbose_name="Correo electrónico",
														max_length=100,
														blank=True, null=True,
														db_index=True,
														validators=[
																EmailValidator(),
																MinLengthValidator(1),
																MaxLengthValidator(100),
															]
														)
	fotografia   					 = models.ImageField(
															blank=True,
															null=True,
															verbose_name='Avatar (Fotografía)',
															upload_to='fotografias',
															help_text='Subir fotografia (Opcional).',
															default='default/No_Avatar_1.png',
														)

	distrito 				= models.ForeignKey(Distrito, related_name='%(app_label)s_%(class)s_related')
	zona					= models.ForeignKey(Zona, blank=True, null=True, default=None, related_name='%(app_label)s_%(class)s_related')
	via						= models.ForeignKey(Via, blank=True, null=True, default=None, related_name='%(app_label)s_%(class)s_related',)
	direccion         	    = models.CharField(
									verbose_name='Dirección',
									max_length=255,
									validators=[
										        MinLengthValidator(1),
										        MaxLengthValidator(255),
										    ],
									db_index=True,
									)
	descripcion		    = models.TextField(verbose_name='Descripción' ,blank=True, null=True, help_text='(Opcional).')
	
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )


	def __unicode__(self):
		return self.get_nombre_completo()

	def get_nombre_completo(self):
		return self.apellido_paterno + ' ' + self.apellido_materno + ', ' + self.nombre

	class Meta:
		abstract = True
