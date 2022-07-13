from .views import (
    UserCreate, UserUpdate, UserDelete, UserListView, TaskCreate, TaskUpdate, TaskDelete, TaskList
)
from django.urls import path

urlpatterns = [
    path(r'users/create', UserCreate.as_view(), name='user-create'),
    path(r'tasks/create', TaskCreate.as_view(), name='task-create'),
    path(r'users/update/<int:pk>', UserUpdate.as_view(), name='user-update'),
    path(r'tasks/update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path(r'users/delete/<int:pk>', UserDelete.as_view(), name='user-delete'),
    path(r'tasks/delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path(r'users', UserListView.as_view(), name='user-list'),
    path(r'tasks', TaskList.as_view(), name='task-list')
]