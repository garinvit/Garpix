from urllib.parse import quote_plus, urlencode
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
# from django.utils.text import slugify
from django.views.generic import ListView
from .slugify import slugify
from .forms import PizzaForm, IngredientsForm
from .models import Pizza, IngredientInfo, Topping
from rest_framework.authtoken.models import Token

# Create your views here.
COUNT = 6


def index(request):
    ordering = '-created_at'
    all_topping = Topping.objects.all()
    if request.method == 'POST':
        post_dict = request.POST.dict().keys()
        lst_ing = []
        for i in post_dict:
            lst_ing.append(i)
        lst_ing = list(map(int, lst_ing[1::]))
        pizzas_objects = Pizza.objects.all()
        pizzas = []
        for pizza in pizzas_objects:
            if set(lst_ing).issubset(pizza.get_topping_id()):
                pizzas.append(pizza)
    if request.method == 'GET':
        tag = request.GET.get('tag')
        topping = request.GET.get('topping_id')
        if tag:
            pizzas = Pizza.objects.filter(tags__name=tag).order_by(ordering)
        elif topping:
            topping = IngredientInfo.objects.all().filter(topping_id=topping)
            pizza_ids = [x.pizza_id for x in topping]
            pizzas = [Pizza.objects.get(pk=x) for x in pizza_ids]
        else:
            pizzas = Pizza.objects.all().order_by(ordering)
    paginator = Paginator(pizzas, 4)
    current_page = request.GET.get('page', 1)
    pizza_page = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if pizza_page.has_previous():
        prev_page = '?' + urlencode({'page': pizza_page.previous_page_number()}, quote_via=quote_plus)
    if pizza_page.has_next():
        next_page = '?' + urlencode({'page': pizza_page.next_page_number()}, quote_via=quote_plus)
    return render(request, 'pizza/index.html', context={
        'pizzas': pizza_page,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
        'toppings': all_topping,
    })


def pizza_view(request, slug):
    pizza = get_object_or_404(Pizza, slug=slug)
    if request.user.id == pizza.author.id:
        is_author = True
    else:
        is_author = False
    context = {
        "pizza": pizza,
        "is_author": is_author,
    }
    return render(request, 'pizza/pizza.html', context)


@login_required(login_url='/users/login')
def add_pizza_view(request):
    add_ingredients = IngredientsForm()
    if request.method == 'POST':
        post = request.POST.copy()
        post["author"] = request.user.id
        post["slug"] = slugify(post['name'])
        add_form = PizzaForm(post, request.FILES, initial={"author": request.user.id})
        if add_form.is_valid():
            pizza = add_form.save()
            # print(pizza.id, len(post.getlist("topping")), post.getlist("topping"), type(post.getlist("topping")))
            for i in range(COUNT):
                # print(post.getlist("topping")[i], post.getlist("measure")[i], post.getlist("count")[i])
                pizza.add_topping(topping=post.getlist("topping")[i], measure=post.getlist("measure")[i], count=post.getlist("count")[i])
            return redirect(f"/pizza/{pizza.slug}")
    else:
        add_form = PizzaForm(initial={"author": request.user.id})
    return render(request, "pizza/add.html", {"form": add_form, "ing_form": add_ingredients, "range": range(COUNT)})


class SearchResultView(ListView):
    model = Pizza
    template_name = "pizza/search_result.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Pizza.objects.filter(
            Q(name__icontains=query)
        )
        print(object_list)
        return object_list


@login_required(login_url='/users/login')
def pizza_edit(request, slug):
    pizza = get_object_or_404(Pizza, slug=slug)
    ingredients = pizza.get_topping()
    if request.user.id != pizza.author.id:
        raise PermissionDenied
    if request.method == "POST":
        post = request.POST.copy()
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.moder = 0
            pizza.save()
            for num, ing in enumerate(ingredients):
                print(num, ing)
                ing.topping = Topping.objects.get(pk=post.getlist("topping")[num])
                ing.measure = post.getlist("measure")[num]
                ing.count = post.getlist("count")[num]
                ing.save()
            return redirect(f"/pizza/{pizza.slug}")
    else:
        form = PizzaForm(instance=pizza)
        ingr_forms = [IngredientsForm(instance=ing) for ing in ingredients]
        context = {'form': form}
        if ingr_forms:
            context["ingredients"] = ingr_forms
    return render(request, 'pizza/edit.html', context)


def profile_view(request):
    #token = Token.objects.get_or_create(user=request.user)
    try:
        token = Token.objects.get(user=request.user)
    except:
        token = Token.objects.create(user=request.user)
    print(token.key)
    pizzas = Pizza.objects.filter(author=request.user.id)
    context = {
        "pizzas": pizzas,
        "token": token.key,
    }
    return render(request, "pizza/profile.html", context)

def api_description(request):
    return render(request, "pizza/api.html")