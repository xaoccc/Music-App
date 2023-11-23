import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicApp.settings")
django.setup()

from musicApp.music.models import Album, Song

album = Album.objects.prefetch_related('song_set').first()


for song in album.song_set.all():

    print(song.name)
# Create your tests here.
