from django.db import models

from account.models import CustomUser
from artists.models import Artist
from categories.models import Category


class Playlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    songs = models.ManyToManyField('Song', related_name='songs')

    def __str__(self):
        return f'{self.title}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    # album_name = models.CharField(max_length=100)
    audio_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='songs', on_delete=models.SET_NULL, null=True)
    duration = models.CharField(max_length=20)
    year = models.DateField()
    # playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, related_name='playlists', blank=True, null=True)
    # number_of_plays = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} - {self.artist_name}'