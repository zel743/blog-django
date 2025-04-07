# settings_template.py
SECRET_KEY = 'tu-secret-key-aqui'  # Reemplazar en producción
DEBUG = True  # Cambiar a False en producción
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}