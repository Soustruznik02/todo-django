from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta(object):
        model = User
        exclude = ['created_at', 'updated_at']


class UserUpdateForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta(object):
        model = User
        exclude = ['created_at', 'updated_at']