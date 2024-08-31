# initialize.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'control_combustible.settings')
django.setup()

from django.core.management import call_command

def run_migrations():
    call_command('migrate')

if __name__ == "__main__":
    run_migrations()