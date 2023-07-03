from django.db import models

from account.models import CustomUser
from artists.models import Artist
from songs.models import Playlist


# Create your models here.

class Follow(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name='followers', on_delete=models.CASCADE)
    # playlist = models.ForeignKey(Playlist, related_name='playlists', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'artist']

