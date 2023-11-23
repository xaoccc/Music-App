from django.urls import path, include
from musicApp.music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('song/create/', views.create_song, name='create_song'),

    path('album/', include([
        path('create/', views.create_album, name='create_album'),
        path('details/<int:album_id>/', views.album_details, name='album_details'),
        path('edit/<int:album_id>/', views.album_edit, name='album_edit'),
        path('delete/<int:album_id>/', views.album_delete, name='album_delete'),

    ])),

]