from django.urls import path, include

from playlists import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('', views.PostListCreateView.as_view()),
    # path('<int:pk>/', views.PostDetailView.as_view()),
]