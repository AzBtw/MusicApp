from rest_framework import serializers

from categories.models import Category
from songs.serializers import SongSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')
    songs = SongSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        children = instance.children.all()
        repr['songs_count'] = instance.songs.count()
        if children is not None:
            repr['children'] = CategoryListSerializer(children, many=True).data
        return repr


