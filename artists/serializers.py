from rest_framework import serializers

from artists.models import Artist
from songs.serializers import SongSerializer


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Artist
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['songs_count'] = instance.songs.count()
        return repr
