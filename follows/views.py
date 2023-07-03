from django.shortcuts import render
from rest_framework import generics, permissions

from account.permissions import IsAuthor
from follows import serializers
from follows.models import Follow


# Create your views here.

class FollowCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.FollowSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class FollowDeleteView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    permission_classes = (IsAuthor,)
