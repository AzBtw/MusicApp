from django.db import models


# Create your models here.

class Song(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    song_length = models.CharField(max_length=100)
    number_of_plays = models.CharField(max_length=100)
