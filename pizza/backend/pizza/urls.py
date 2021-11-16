from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "pizza"

urlpatterns = [
    path("", views.index, name="index"),
    path("pizza/<slug:slug>", views.pizza_view, name="pizza"),
    path("pizza/add/", views.add_pizza_view, name="add"),
    path("search/", views.SearchResultView.as_view(), name="search_results"),
    path("pizza/<slug:slug>/edit", views.pizza_edit, name="pizza_edit"),
    path("user/", views.profile_view, name="profile"),
    path("api/", views.api_description, name="api_description"),
]
