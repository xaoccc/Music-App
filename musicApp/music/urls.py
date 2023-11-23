from django.urls import path, include
from musicApp.music import views

urlpatterns = [
    path('', views.index, name='index')

]