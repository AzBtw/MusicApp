from django.urls import path, include

from songs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', views.SongViewSet)
router.register('playlists', views.PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls))
]