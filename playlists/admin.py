from django.contrib import admin

from playlists.models import Playlist, PostPlaylist

# Register your models here.

admin.site.register(Playlist)
admin.site.register(PostPlaylist)
