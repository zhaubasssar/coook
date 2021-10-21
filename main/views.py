from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Recipe


class HomeView(TemplateView):
    template_name = "home.html"


class FeedpageView(TemplateView):

    def get(self, request, *args, **kwargs):
        data = Recipe.objects.all()
        return render(request, "feedpage.html", {'recipes': data})


def hello(request):
    # При обращении
    return HttpResponseRedirect('home')


class RecipeArticle(DetailView):
    model = Recipe
    template_name = "recipe_article.html"
