import os
import dj_database_url
from pathlib import Path

# Directorio Base
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Seguridad
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-cambiar-en-produccion")
DEBUG = "RENDER" not in os.environ

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
else:
    ALLOWED_HOSTS = ["*"]

# 📦 Apps Instaladas - El orden aquí es CRÍTICO para Cloudinary
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic", #
    "django.contrib.staticfiles",
    "cloudinary_storage",            # Debe ir antes de staticfiles
    "cloudinary",
    "perfil",                        # Asegurar que la carpeta se llame 'perfil'
]

# ⚙️ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", #
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hoja_de_vida.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hoja_de_vida.wsgi.application"

# 🗄️ Base de Datos (Segura con Variables de Entorno)
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get('DATABASE_URL'), #
        conn_max_age=600,
    )
}

# 🌍 Idioma y Zona Horaria
LANGUAGE_CODE = "es-ec"
TIME_ZONE = "America/Guayaquil"
USE_I18N = True
USE_TZ = True

# 📁 Configuración de Cloudinary (Credenciales desde Render)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# 📁 Manejo de Archivos (Estáticos y Multimedia)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/media/"

# Configuración de Almacenamiento Django 4.2+
STORAGES = {
    "default": {
        # RawMedia permite subir PDFs e Imágenes sin errores 401 de permisos
        "BACKEND": "cloudinary_storage.storage.RawMediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage", #
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Permite cargar el PDF dentro de la web
X_FRAME_OPTIONS = 'SAMEORIGIN'