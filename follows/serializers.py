from rest_framework import serializers

from follows.models import Follow


class FollowArtistSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='owner.id')
    # owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Follow
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.id')
    # owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Follow
        fields = ('artist', )

    # def validate(self, attrs):
    #     user = self.context['request'].user
    #     post = attrs['post']
    #     if user.likes.filter(post=post).exists():
    #         raise serializers.ValidationError("You've already liked this post.")
    #     return attrs
