from django import forms
from django.db import models


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default = False, null = False)
    title = models.CharField(max_length = 70, blank=False, null=False)

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = False, null = False)
    email = models.EmailField(max_length = 254, blank=False, null=False)
    password = models.CharField(max_length = 50, blank=False, null=False)
    