from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers
from pizza.models import Pizza, Tag, IngredientInfo, Topping


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ["id", "name", "description"]


class IngredientSerializer(serializers.ModelSerializer):
    topping = ToppingSerializer()
    class Meta:
        model = IngredientInfo
        fields = ["id", "topping", "count", "measure"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class GeneralSerializer(serializers.ModelSerializer):
    ingredientinfo_set = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = Pizza
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
