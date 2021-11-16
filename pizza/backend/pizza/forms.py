from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.forms.models import inlineformset_factory, BaseInlineFormSet

from .models import Pizza, Tag, IngredientInfo, Topping


class PizzaForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Pizza
        fields = '__all__'


class IngredientsForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput())
    topping = forms.ModelChoiceField(queryset=Topping.objects.all())

    class Meta:
        model = IngredientInfo
        fields = '__all__'



# class ToppingCategoryForm(forms.ModelForm):
#     check = forms.CheckboxInput()
#     class Meta:
#         model = Topping
#         fields = ['name']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-input'}),
        #     'ingredients': forms.CheckboxSelectMultiple(attrs={'cols': 60, 'rows': 10}),
        # }
