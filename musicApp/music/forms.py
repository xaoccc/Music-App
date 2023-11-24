from django import forms

from musicApp.music.models import Album, Song

class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    class Meta:
        model = Album
        fields = ['name']


class SongBaseForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'album']

class SongCreateForm(SongBaseForm):
    pass


