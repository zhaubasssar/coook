from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Recipe
from main.forms import RecipeForm


def hello(request):
    # При обращении по url / срабатывает редирект на вьюшку с адресом /home/
    return HttpResponseRedirect('home')


class HomeView(TemplateView):
    template_name = "home.html"


class CreateRecipe(CreateView):
    model = Recipe
    template_name = "new_recipe.html"
    form_class = RecipeForm
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return HttpResponseRedirect(self.success_url)


class FeedpageView(LoginRequiredMixin, ListView):
    model = Recipe
    login_url = reverse_lazy('login')
    template_name = "feedpage.html"

    def get(self, request, *args, **kwargs):
        recipe_list = self.model.objects.filter(checked=True)
        return render(request, self.template_name, {'recipe_list': recipe_list})


class MyReceiptsView(LoginRequiredMixin, ListView):
    model = Recipe
    login_url = reverse_lazy('login')
    template_name = "my_receipts.html"

    def get(self, request, *args, **kwargs):
        recipe_list = self.model.objects.filter(checked=True, author=request.user)
        return render(request, self.template_name, {'recipe_list': recipe_list})


class RecipeArticle( LoginRequiredMixin, DetailView):
    model = Recipe
    login_url = reverse_lazy('login')
    template_name = "recipe_article.html"
