from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from todo.models import User, Task
from todo.forms import UserCreateForm, UserUpdateForm
from django.urls import reverse_lazy


###USERS###
class UserList(ListView):
    model = User
    paginate_by = 15
    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserCreate(CreateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserCreateForm
    success_url=reverse_lazy("user-list")

class UserUpdate(UpdateView):
    model = User
    template_name = 'update_user.html'
    form_class = UserUpdateForm
    success_url=reverse_lazy("user-list")

class UserDelete(DeleteView):
    model = User
    template_name='delete_user.html'
    success_url=reverse_lazy("user-list")

###TASKS###
class TaskList(ListView):
    model = Task
    paginate_by = 15
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TaskCreate(CreateView):
    model = Task
    fields =[
        'owner',
        'is_completed',
        'title'
    ]
    template_name = 'create_task.html'
    success_url=reverse_lazy("task-list")

class TaskUpdate(UpdateView):
    model = Task
    fields = [
        'owner',
        'is_completed',
        'title'
    ]
    template_name = 'update_task.html'
    success_url=reverse_lazy("task-list")

class TaskDelete(DeleteView):
    model = Task
    success_url=reverse_lazy("task-list")