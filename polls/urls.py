from django.urls import path
from .views import (
    DashboardView,
    PollCreateView,
    PollUpdateView,
    PollDeleteView,
    PollDetailView,
    PollVoteView,
)

app_name = 'polls'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/', PollCreateView.as_view(), name='poll_create'),
    path('<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
    path('<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('<int:pk>/vote/', PollVoteView.as_view(), name='poll_vote'),
]
