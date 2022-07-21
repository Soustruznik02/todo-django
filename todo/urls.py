from .views import (
    UserCreateView, UserUpdateView, UserDeleteView, UserListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskListView
)
from django.urls import path

urlpatterns = [
    path(r'users/create', UserCreateView.as_view(), name='user-create'),
    path(r'tasks/create', TaskCreateView.as_view(), name='task-create'),
    path(r'users/update/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path(r'tasks/update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path(r'users/delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
    path(r'tasks/delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
    path(r'users', UserListView.as_view(), name='user-list'),
    path(r'tasks', TaskListView.as_view(), name='task-list')
]