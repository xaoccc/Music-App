from django.shortcuts import render, redirect

from musicApp.music.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, SongCreateForm
from musicApp.music.models import Album, Song


# Create your views here.
def index(request):
    albums = Album.objects.all()

    context = {
        'albums': albums
    }

    return render(request, 'common/index.html', context)




def create_album(request):

    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form
    }


    return render(request, 'albums/create-album.html', context)


def album_details(request, album_id):
    album = Album.objects.prefetch_related('song_set').filter(pk=album_id).get()
    songs = album.song_set.all()

    context = {
        'album': album,
        'songs': songs
    }

    return render(request, 'albums/album-details.html', context)

def album_edit(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'albums/edit-album.html', context)

def album_delete(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)

    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect('index')

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'albums/delete-album.html', context)

def create_song(request):
    if request.method == 'GET':
        form = SongCreateForm()
    else:
        form = SongCreateForm(request.POST)


        if form.is_valid():
            song_name = form.cleaned_data['song_name']
            album_id = form.cleaned_data['album']

            # Get the Album object
            album = Album.objects.get(pk=album_id)

            # Create a new Song object
            song = Song(name=song_name, album=album)
            song.save()

            return redirect('index')

    context = {
        'form': form
    }


    return render(request, 'songs/create-song.html', context)