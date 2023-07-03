from django.urls import path, include

from categories import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.CategoryCreateListView.as_view()),
    path('<int:pk>/', views.CategoryDetailView.as_view()),
]
