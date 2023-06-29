from rest_framework import serializers

from playlists.models import Playlist, PostPlaylist


class PlaylistListSerializer(serializers.ModelSerializer):
    # owner_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Playlist
        fields = ('id', 'title', 'preview')


class PostPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPlaylist
        fields = '__all__'


class PlaylistCreateSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='user.id')
    songs = PostPlaylistSerializer(many=True, required=False)

    class Meta:
        model = Playlist
        fields = '__all__'

    def create(self, validated_data):
        # print(self, '!!!')
        # print(validated_data, '***')
        # print(self)
        # print(validated_data)
        request = self.context.get('request')
        # print(request.FILES.getlist('images'))
        songs = request.FILES.getlist('songs')
        # print(images)
        playlist = Playlist.objects.create(**validated_data)
        # return images
        for song in songs:
            PostPlaylist.objects.create(song=song, playlist=playlist)
        return playlist


class PostDetailSerializer(serializers.ModelSerializer):
    # owner_username = serializers.ReadOnlyField(source='user.username')
    songs = PostPlaylistSerializer(many=True)
    # comments = CommentSerializer(many=True)  # 1 способ - related name
    # likes = LikeSerializer(many=True)

    class Meta:
        model = Playlist
        fields = '__all__'

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     repr['comments_count'] = instance.comments.count()
    #     repr['likes_count'] = instance.likes.count()
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         repr['is_liked'] = user.likes.filter(post=instance).exists()
    #         repr['is_favorite'] = user.favorites.filter(post=instance).exists()
    #     # repr['comments'] = CommentSerializer(instance.comments.all(), many=True).data # 2 способ
    #     return repr