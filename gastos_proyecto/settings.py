import os
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db  # Asegúrate de que importas la base de datos en tiempo real si la usas

# Definir la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración del archivo de credenciales de Firebase
FIREBASE_CREDENTIALS = os.path.join(BASE_DIR, 'gastos_proyecto/config/serviceAccountKey.json')

# Verificar si el archivo de credenciales existe
if not os.path.exists(FIREBASE_CREDENTIALS):
    raise FileNotFoundError(f"El archivo de credenciales no se encuentra en: {FIREBASE_CREDENTIALS}")

# Inicializar Firebase Admin con las credenciales
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://elmirador1-aa06b-default-rtdb.firebaseio.com/'  # Reemplaza con la URL real de tu base de datos de Firebase
})

# Obtener la referencia a Firestore y Realtime Database
db_firestore = firestore.client()
db_realtime = db.reference()

# Configuración del Proyecto
SECRET_KEY = 'nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDe8vFphX436V9N\njwZ6CpJwa/R0h074Rohl7yd7l45mckEImLx2OVI8L2TPdXMz/5yfVlK5AYGBQlh7\nMi5QhNjlsFeE+xAh9vqBpQDPvAHCsblxZYURmxL9AJ6+oJ31ZTFO8bYkNjIUS4MJ\nKtxX3iJSy/QRe4HnmOEwouwiLeC3pLDodajtvFY48Skx6Py4x7PCSTCwQ4WXXM4c\nj9MwmMlGWeUoH6DyddBYbnkdTjQVEDpty4XG06IUZTL9R1yBl+Y4gNPXPHLNqpFx\n0TbmsQldTPTKuzS/E3GggVkBPFsdHHVRk9tBXrn6XuQs9VNIDb76h9t0M1os5BoY\nclg7nLUBAgMBAAECggEABCdF/eeDAF3Rt53tFWEfinEfFXxU1Aq/rUMikD/0ou4e\nIzUcjl5HLNWxh4I3t8sGBbDjwHcUTM5p3BJaqweCi+rjAoLz3BIgEhdlwmOiq8LI\nV+INM9St//Z0PqG64kYKQF8qkRZNDLQ9wsdgjKbX1a+KLTjeD2y5cJYZwebqu2O7\nki/u56vuUtI+AJcEUv8AzOxjhrvbS2L1xUuw2fk/BL6K2y4yuMQVD9xVTYDXssSJ\nKr5UyUZNCZBnJLlLmVekAHmsx+VUf4DErKLhzWTkkqygCZZUmH9xbG4mAbljh9gZ\nec6+Re4ArIpoCyzhziBGKOUWSJM0sI7C5ObYqhMiTQKBgQDwIRJxrLs7dULcBG3p\nnS4jNG6/bNwaFugAfEL0IrtX9EoAkvroNcNNYJF71aHcD3X1r93IUQ2VIiOVRIVu\nXY3HeZh5ry5rMRplYGjbH2+NhMEA2VkL1PknYhULgz24E9gR8Y4jTyvYsgIj3GD8\nT/20uq5FSUnWWvr8HwEXvGqfNQKBgQDtry+ve4n9nlydw60rvgg2dc4v0WGCD6X1\nFFkSWyDoitHcAkmF8zPQgkFtEqn6RcAGO+2p+QOc+Kn+E85JN5yYgnuvW8UMhYey\nBSohvoxUFIsI6yxWw+Xr/CZIhYM4+jZ/8h9RPLvrCoZ1pu4fBKBy1/R1O0lsGyI2\nULka+x98HQKBgAaLQC9s36VdKrdIP56QNAOtmB8LXmwvl577w+9XSve4ppOhbckK\nPgpLyWswhTq0CSjq5AZjfxVDWujkdyZs0kJPZAJc7czqB6gfmnvuPWID7iaRxcV2\nxlt2ZtBrgTEVCVxj0tXPgIhlQX2ssc/udiGIvNsShjqbPB/G0IbPEbDJAoGBAJul\n3l9XUk0QeGwj6PI9NpmbWdO8lNMcNjyg/5dir9E4nycpJEagtey0b+3ijAdFx/MN\nKZzmYfRYbtHg3HTcAyNoR2DVgtupUexFL4r7gl/JOCc2AkorbRS1gch6Di2wxSHS\nR6nmUNUhhl3jXApZ+ExcmUxv76votOXGxQEjNEINAoGAZDxaogY0Jb5Oq8w/Wez2\nXkSqg9hcVyW8C2W3R8nLsf1JfYvUhynsk/5wNWxXdNGJ6Ghu93+ECFfZYTzOxpLO\nLSu56iUCxluuWoVoQlWjpoi/KgZeIIWRBdB8y5WaMyTIMuFP7nyxva1AHrblaRa4\nFwXN2C6M7Lm2zj5abQ8WWhc=\n-----END PRIVATE KEY-----\n'
DEBUG = True
ALLOWED_HOSTS = []

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Si estás utilizando Django REST Framework
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs
ROOT_URLCONF = 'gastos_proyecto.urls'

# Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'gastos', 'templates')],  # Asegúrate de que esta línea esté correcta
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

# WSGI Application
WSGI_APPLICATION = 'gastos_proyecto.wsgi.application'

# Base de datos (Si no usas Firebase para la base de datos, configura PostgreSQL, SQLite, etc.)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Contraseñas
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

# Idioma y zona horaria
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'

# Archivos de medios (si usas imágenes, videos, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración de CORS si estás trabajando con una API (si usas DRF y quieres permitir solicitudes desde otros dominios)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Si usas React o cualquier otro framework frontend en localhost
    "https://tu-aplicacion.com",  # Agrega el dominio de tu aplicación
]
