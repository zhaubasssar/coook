from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="sign_up")
]