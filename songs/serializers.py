from rest_framework import serializers

from songs.models import Song, Playlist


# Song Serializers

class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.StringRelatedField()

    class Meta:
        model = Song
        fields = ('title', 'artist_name', 'image', 'duration')


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artist_name', 'image', 'duration',)


class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


# Playlist serializer

class PlaylistListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Playlist
        fields = ('user', 'title', 'image')


class PlaylistDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    songs = serializers.SlugRelatedField(slug_field=Playlist.songs, many=True, queryset=Song.objects.all())

    class Meta:
        model = Playlist
        fields = '__all__'


class PlaylistCreateSerializer(serializers.ModelSerializer):
    songs = serializers.SlugRelatedField(slug_field=Playlist.songs, many=True, queryset=Song.objects.all())

    # artist_name =
    class Meta:
        model = Playlist
        fields = '__all__'
