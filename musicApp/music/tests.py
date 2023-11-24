import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicApp.settings")
django.setup()

from musicApp.music.models import Album, Song


# Create your tests here.
