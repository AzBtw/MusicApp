from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from account.permissions import IsAdmin
from songs import serializers
from songs.models import Song, Playlist


# Create your views here.

class StandartResultPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title', 'artist_name', 'title' + 'artist_name', 'artist_name' + 'title')
    filterset_fields = ('artist_name',)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SongListSerializer
        elif self.action == ('create', 'update', 'partial_update'):
            return serializers.SongCreateSerializer
        return serializers.SongDetailSerializer

    def get_permissions(self):
        # может удалять только админ
        if self.action == 'destroy':
            return [IsAdmin(), ]

        if self.action == 'create':
            return [IsAdmin(), ]


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PlaylistListSerializer
        elif self.action == ('create', 'update', 'partial_update'):
            return serializers.PlaylistCreateSerializer
        return serializers.PlaylistDetailSerializer
