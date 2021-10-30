from django.urls import path
from main.views import *

urlpatterns = [
    path('', hello, name="hello"),
    path('home/', HomeView.as_view(), name="home"),
    path('feedpage/', FeedpageView.as_view(), name="feed"),
    path('recipe/<str:slug>/', RecipeArticle.as_view(), name="recipe-article"),
]