from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['type'] = "text"
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['username'].widget.attrs['placeholder'] = "Username"

        self.fields['password1'].widget.attrs['placeholder'] = "Password"
        self.fields['password1'].widget.attrs['type'] = "password"
        self.fields['password1'].widget.attrs['class'] = "form-control"

        self.fields['password2'].widget.attrs['placeholder'] = "Confirm password"
        self.fields['password2'].widget.attrs['type'] = "password"
        self.fields['password2'].widget.attrs['class'] = "form-control"
