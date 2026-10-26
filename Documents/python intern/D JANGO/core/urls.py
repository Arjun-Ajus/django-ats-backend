from django.urls import path
from .views import JobListCreateAPIView, UserTestAPIView

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('users/', UserTestAPIView.as_view(), name='user-test'),
]