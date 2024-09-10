# Importações padrões
from pathlib import Path, os

# Importamos todas as configurações do arquivo base
from .settings import *

# Definimos que estamos em momento de desenvolvimento, deixando o DEBUG como True
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m#p#*9!d3@l(6cu1t%41kt)*1=hgl&b@5)+^2p*!7p_wj5lk7m'

ALLOWED_HOSTS = ['www.ergogroupapp.com']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ErgoGroup$ErgoGroupApp',
        'USER': 'ErgoGroup',
        'PASSWORD': 'Ergo#%2024',
        'HOST': 'ErgoGroup.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}