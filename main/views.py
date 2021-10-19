from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from main.models import Recipe


class HomeView(TemplateView):
    template_name = "home.html"


class FeedpageView(TemplateView):

    def get(self, request, *args, **kwargs):
        data = Recipe.objects.all()
        return render(request, "feedpage.html", {'data': data})


def hello(request):
    # При обращении
    return HttpResponseRedirect('home')
