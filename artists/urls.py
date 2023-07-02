from django.urls import path, include

from artists import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ArtistViewSet)

urlpatterns = [
    path('', include(router.urls))
]