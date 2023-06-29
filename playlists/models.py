from django.db import models

from account.models import CustomUser


# Create your models here.

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    user_id = models.ForeignKey(CustomUser, related_name='playlists', on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f'{self.title}'

    class Meta:
        ordering = ('created_at',)


class PostPlaylist(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    song = models.ForeignKey(Playlist, related_name='songs', on_delete=models.CASCADE)

