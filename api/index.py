from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "control_combustible.settings")  # Cambia `nombre_proyecto` al nombre de tu proyecto
app = get_wsgi_application()
