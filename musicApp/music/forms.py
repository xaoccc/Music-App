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

class SongBaseForm(forms.Form):
    song_name = forms.CharField(label='Song Name', max_length=30, required=True)
    album = forms.ChoiceField(label='Album', choices=[])

    def __init__(self, *args, **kwargs):
        super(SongBaseForm, self).__init__(*args, **kwargs)

        albums = Album.objects.all()
        self.fields['album'].choices = [(album.id, album.name) for album in albums]


# class SongBaseForm(forms.ModelForm):
#     album = forms.ModelChoiceField(queryset=Album.objects.values_list('id', flat=True), empty_label="Album name")
#     class Meta:
#         model = Album
#         fields = ['name', 'album']

class SongCreateForm(SongBaseForm):
    pass


