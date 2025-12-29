#!/usr/bin/env bash
# Salir si ocurre un error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos (CSS, Imágenes)
python manage.py collectstatic --no-input

# Aplicar migraciones de la base de datos
python manage.py migrate


# ESTO CREA TU USUARIO GRATIS
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'dayanamolina@gmail.com', '123')
    print('Usuario creado')
EOFÑ