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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}

'''
    ====================================
    ARQUIVO DE CONFIGURAÇÕES DO SERVIDOR
    ====================================

    from pathlib import os
    from dotenv import load_dotenv
    from .settings import *

    load_dotenv()

    DEBUG = True

    SECRET_KEY = str(os.getenv('SECRET_KEY'))

    ALLOWED_HOSTS = [ 'www.ergogroupapp.com']

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
'''