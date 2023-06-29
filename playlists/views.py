from django.shortcuts import render
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from playlists import serializers
from playlists.models import Playlist
from playlists.permissions import IsAuthorOrAdmin, IsAuthor


# Create your views here.

class StandartResultPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'page'


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title', 'body')
    filterset_fields = ('user_id', 'id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PlaylistListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.PlaylistCreateSerializer
        return serializers.PlaylistDetailSerializer

    def get_permissions(self):
        # удалять может только автор поста или админы
        if self.action == 'destroy':
            return [IsAuthorOrAdmin(), ]
        # обновлять может только автор поста
        elif self.action in ('update', 'partial_update'):
            return [IsAuthor(), ]
        # просматривать могут все (list, retrieve)
        # но создавать может залогиненный пользователь
        return [permissions.IsAuthenticatedOrReadOnly(), ]