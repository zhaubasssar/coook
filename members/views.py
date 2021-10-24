from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.shortcuts import render, get_object_or_404


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    context_object_name = "form"

    def form_valid(self, form):
        member = form.save()
        member.save()
        return HttpResponseRedirect(self.success_url)
