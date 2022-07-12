from django.contrib import admin
from todo.models import (Task, User)


class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
