from artists import serializers
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from account.permissions import IsAdmin
from artists.models import Artist


class StandartResultPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    search_fields = ('artist_name', )

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ArtistListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.ArtistCreateSerializer
        return serializers.ArtistDetailSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'create', 'update', 'partial_update'):
            return [IsAdmin(), ]
        return [permissions.IsAuthenticatedOrReadOnly(), ]
