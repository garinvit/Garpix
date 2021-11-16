from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import PizzaView, PizzaCreate, PizzaModelView

app_name = "api"

urlpatterns = [
    path("general/", PizzaView, name="api_pizzas"),
    path("pizzas/create", PizzaCreate, name="api_pizzas_create"),
    path("pizzas/", PizzaModelView.as_view(), name="pizza_model")
]
