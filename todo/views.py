from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from todo.models import User, Task
from todo.forms import UserCreateForm, UserUpdateForm
from django.urls import reverse_lazy


###USERS###
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserCreateView(CreateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserCreateForm
    success_url=reverse_lazy("user-list")

class UserUpdateView(UpdateView):
    model = User
    template_name = 'update_user.html'
    form_class = UserUpdateForm
    success_url=reverse_lazy("user-list")

class UserDeleteView(DeleteView):
    model = User
    template_name='delete_user.html'
    success_url=reverse_lazy("user-list")

###TASKS###
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TaskCreateView(CreateView):
    model = Task
    fields =[
        'owner',
        'is_completed',
        'title'
    ]
    template_name = 'create_task.html'
    success_url=reverse_lazy("task-list")

class TaskUpdateView(UpdateView):
    model = Task
    fields = [
        'owner',
        'is_completed',
        'title'
    ]
    template_name = 'update_task.html'
    success_url=reverse_lazy("task-list")

class TaskDeleteView(DeleteView):
    model = Task
    success_url=reverse_lazy("task-list")
    template_name = 'delete_task.html'