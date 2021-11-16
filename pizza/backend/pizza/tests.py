import json

from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework.test import APIClient

from .models import Pizza, Tag, Topping, IngredientInfo

# Create your tests here.


class PizzaTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(id=1, username="admin")
        tag = Tag.objects.create(name="Акция")
        topping = Topping.objects.create(name="ЯдерКола", description="Популярнейший в США безалкогольный напиток, который выпускался до Великой войны.")
        topping_2 = Topping.objects.create(name="Камень", description="Попал случайно")
        pizza_1 = Pizza.objects.create(author=user, name="4 сыра", description="Пицца из смеси сыров", slug="4-syra")
        ingredientinfo = IngredientInfo.objects.create(pizza=pizza_1, topping=topping, count="111", measure="gr")

    def test_pizza_methods(self):
        pizza = Pizza.objects.get(slug="4-syra")
        topping = Topping.objects.get(name="Камень")
        # print(pizza, topping)
        pizza.add_topping(topping=topping.id, count=111, measure="gr")
        self.assertEqual(len(pizza.get_topping()), 2)
        self.assertEqual(list(pizza.get_topping()), list(pizza.ingredientinfo_set.all()))
        self.assertQuerysetEqual(pizza.get_topping().order_by('-topping'), pizza.ingredientinfo_set.all().order_by('-topping'))
        ids = pizza.get_topping_id()
        self.assertEqual(len(ids), 2)
        self.assertEqual(ids, [x.id for x in pizza.get_topping()])
        self.assertEqual(pizza.get_absolute_url(), "/pizza/4-syra/")

    def test_index_view(self):
        c = Client()
        response = c.get("")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["toppings"].count(), 2)

    def test_pizza_view(self):
        pizza = Pizza.objects.get(slug="4-syra")
        c = Client()
        response = c.get(f"http://127.0.0.1:8000/pizza/{pizza.slug}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["pizza"], pizza)


    def test_pizza_view(self):
        pizza = Pizza.objects.get(slug="4-syra")
        c = Client()
        response = c.get(f"http://127.0.0.1:8000/pizza/{pizza.slug}/edit")
        self.assertEqual(response.status_code, 302)


    def test_profile_view(self):
        user = User.objects.get(username="admin")
        c = Client()
        c.force_login(user)
        response = c.get("http://127.0.0.1:8000/user/")
        # print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["pizzas"], Pizza.objects.filter(author=user))

    def test_api_get(self):
        user = User.objects.get(username="admin")
        c = Client()
        c.force_login(user)
        response = c.get("/api/v1/general/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["pizzas"][0]["slug"], '4-syra')
        response = c.get("/api/v1/pizzas/")
        self.assertEqual(response.status_code, 401)#  не авторизован
    # Не могу авторизоваться по токену так как не получается добавить собственный заголовок к запросу, а во вью присваивается автор из запроса
    #     response = c.get("http://127.0.0.1:8000/api/v1/pizzas/")
    #     print("a", response.headers, "b", response.json())


    def test_api_post(self):
        user = User.objects.get(username="admin")
        c = Client()
        c.force_login(user)

        data = {
            "pizza":
                {
                    "author": 1,
                    "name": "Карбонара",
                    "description": "Пицца из смеси пицц",
                    "slug": "carbonara",
                    "tags": [
                        1]
                }
        }
        response = c.post("http://127.0.0.1:8000/api/v1/pizzas/create", content_type="application/json", data=data, )
        # print(response.json())
        self.assertEqual(response.status_code, 200)
        pizza = Pizza.objects.get(pk=2)
        self.assertEqual(pizza.name, "Карбонара")