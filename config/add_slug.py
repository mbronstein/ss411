import os, django
from config.settings import local
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ss411.config.settings.local')
from ss411.ssoffices.models import SsOffice

django.setup()

def add_slugs():
    lst = SsOffice.objects.all()
    for rec in lst:
        print(rec)

if __name__ == "__main__":
    add_slugs()


