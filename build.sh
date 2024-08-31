
#!/bin/bash

# Activar el entorno virtual
source ./bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Desactivar el entorno virtual
deactivate