from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Recipe


def hello(request):
    # При обращении по url / срабатывает редирект на вьюшку с адресом /home/
    return HttpResponseRedirect('home')


class HomeView(TemplateView):
    template_name = "home.html"


class FeedpageView(LoginRequiredMixin, ListView):
    model = Recipe
    login_url = reverse_lazy('login')
    template_name = "feedpage.html"


class RecipeArticle( LoginRequiredMixin, DetailView):
    model = Recipe
    login_url = reverse_lazy('login')
    template_name = "recipe_article.html"
