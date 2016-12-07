import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q_l1yjc^4_(2k_&7oc)7b$#%jk2%#t_1^qobyaxae70qd%1b7u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pure_pagination',
    'widget_tweaks',
    'rest_framework',
    'index.apps.IndexConfig',
    'infos_sistemas.apps.InfosSistemasConfig',
     #MAIN
    'modulos.apps.ModulosConfig',
    'grupos_modulos.apps.GruposModulosConfig',
    'catalogos_modulos_menus_sub_menus.apps.CatalogosModulosMenusSubMenusConfig',
    'menus.apps.MenusConfig',
    'sub_menus.apps.SubMenusConfig',
 
    'paises.apps.PaisesConfig',
    'departamentos.apps.DepartamentosConfig',
    'provincias.apps.ProvinciasConfig',
    'distritos.apps.DistritosConfig',
    'vias.apps.ViasConfig',
    'zonas.apps.ZonasConfig',

    'estados_civiles.apps.EstadosCivilesConfig',
    'documentos_identificaciones.apps.DocumentosIdentificacionesConfig',
    'entidades.apps.EntidadesConfig',
    'sedes.apps.SedesConfig',
    'areas.apps.AreasConfig',
    'usuarios.apps.UsuariosConfig',
    'tipos_empleados.apps.TiposEmpleadosConfig',
    'cargos.apps.CargosConfig',
    'empleados.apps.EmpleadosConfig',

    'tipos_pilotos.apps.TiposPilotosConfig',
    'pilotos.apps.PilotosConfig',

    'partes_aeronaves.apps.PartesAeronavesConfig', 
    'modelos.apps.ModelosConfig', 
    'marcas.apps.MarcasConfig', 
    'colores.apps.ColoresConfig', 
    'averias.apps.AveriasConfig',
    'tipos_aeronaves.apps.TiposAeronavesConfig',
    'aeronaves.apps.AeronavesConfig',
    'soluciones.apps.SolucionesConfig',
    'catalogos_aeronaves_partes.apps.CatalogosAeronavesPartesConfig',
    'catalogos_aeronaves_partes_averias.apps.CatalogosAeronavesPartesAveriasConfig',
    'catalogos_aeronaves_partes_averias_soluciones.apps.CatalogosAeronavesPartesAveriasSolucionesConfig',
    'catalogos_aeronaves_partes_averias_soluciones_empleados.apps.CatalogosAeronavesPartesAveriasSolucionesEmpleadosConfig',


]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app_aeronaves_light.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app_aeronaves_light.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'App_Aeronaves',
        'USER': 'sa',
        'PASSWORD': 'S1st3mas',
        'HOST': 'localhost',
        'PORT': '1433',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
#MEDIA -> STATIC
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

STATICFILES_FINDERS = {
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
}

#Activar cache para archivos estaticos
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFileStorage'

#Imagenes, audios y videos
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL  = '/media/'

#Configuración de Usuario
AUTH_USER_MODEL = 'usuarios.Usuario'
