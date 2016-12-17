# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from tipos_aeronaves.models import TipoAeronave
from partes_aeronaves.models import ParteAeronave
from modelos.models import Modelo
from marcas.models import Marca
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify



class Aeronave(models.Model):
    BOOL_ACTIVO                     = ((True, 'Si'), (False, 'No'))
    parte_aeronave 	                = models.ManyToManyField(ParteAeronave, through='catalogos_aeronaves_partes.CatalogoAeronaveParte')
    tipo_aeronave                   = models.ForeignKey(TipoAeronave)
    marca                           = models.ForeignKey(Marca)
    modelo                          = models.ForeignKey(Modelo)
    fotografia   					= models.ImageField(
															blank=True,
															null=True,
															verbose_name='Avatar (Fotografía)',
															upload_to='fotografias_aviones',
															help_text='Subir fotografia (Opcional).',
															default='default/No_Avatar_1.png',
															
														)
    numero_cola_aeronave            = models.CharField(
                                      max_length=100,
                                      default= 0,
                                      validators=[
                                                MinLengthValidator(1),
                                                MaxLengthValidator(100),
                                            ],
                                      unique=True, 
                                      db_index=True, 
                                      help_text='Escribir el numero cola de aeronave .')

    descripcion		                = models.TextField(verbose_name='Descripción (Aeronave)' ,blank=True, null=True, help_text='(Opcional).')
    activo                          = models.BooleanField(choices=BOOL_ACTIVO, default=True)
    
    slug                            = models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )


    #Métodos
    #Python 3.X
    def __str__(self):
    	return self.get_nombre()

    #Python 2.X
    #def __unicode__(self):
    #	return self.nombre

    def get_nombre(self):
    	return ' %s | %s | %s | %s ' %(self.tipo_aeronave, self.marca, self.modelo, self.numero_cola_aeronave)

    def save(self, *args, **kwargs):
    	if not self.pk:
    		self.slug = slugify(self.get_nombre())
    	else:
    		slug = slugify(self.get_nombre())
    		if self.slug != slug:
    			self.slug = slug
    	super(Aeronave, self).save(*args, **kwargs)

    #Opciones
    class Meta:
    	#Nombre para la tabla del gestor de base de datos
    	db_table = 'Aeronaves'
    	#Ordenar los registros por un campo especifico
    	ordering = ('tipo_aeronave', 'marca', 'modelo')
    	#Nombre para el Conjunto de Objetos en el Panel de Administración
    	verbose_name = 'Aeronave'
    	#Nombre en Plural en la lista de módulos en el Panel de Administración
    	verbose_name_plural = 'Aeronaves'
