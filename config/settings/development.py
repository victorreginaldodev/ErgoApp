# Importações padrões
from pathlib import os
from dotenv import load_dotenv

load_dotenv()

# Importamos todas as configurações do arquivo base
from .settings import *

# Definimos que estamos em momento de desenvolvimento, deixando o DEBUG como True
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ergoapp',  
        'USER': 'root',    
        'PASSWORD': '101508',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}