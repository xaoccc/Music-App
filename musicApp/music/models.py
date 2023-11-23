from django.db import models

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image_url = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Song(models.Model):
    name = models.CharField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

