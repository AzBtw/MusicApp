from django.urls import path
from follows import views

urlpatterns = [
    path('', views.FollowCreateView.as_view()),
    path('<int:pk>', views.FollowDeleteView.as_view()),
]
