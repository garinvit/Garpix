from rest_framework import viewsets, authentication, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import IngredientSerializer, GeneralSerializer, PizzaSerializer
from pizza.models import Pizza, IngredientInfo, Topping
from pizza.slugify import slugify


@api_view(['GET'])
def PizzaView(request):
    pizzas = Pizza.objects.all()
    serializer = GeneralSerializer(pizzas, many=True)
    return Response({'pizzas': serializer.data})


#без аутентификации
@api_view(['POST'])
def PizzaCreate(request):
    pizza = request.data.get('pizza')
    pizza["author"] = request.user.id
    pizza["slug"] = slugify(pizza['name'])
    serializer = PizzaSerializer(data=pizza)
    if serializer.is_valid(raise_exception=True):
        pizza_inst = serializer.save()
    return Response({"success": f"Pizza {pizza_inst.name} created successfully"})

#с аутентификацией по токену, токен в профиле пользователя
class PizzaModelView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response({'pizzas': serializer.data})

    def post(self, request):
        pizza = request.data.get('pizza')
        print(request.user.id)
        pizza["author"] = request.user.id
        pizza["slug"] = slugify(pizza['name'])
        serializer = PizzaSerializer(data=pizza)
        if serializer.is_valid(raise_exception=True):
            pizza_inst = serializer.save()
        return Response({"success": f"Pizza '{pizza_inst.name}' created successfully"})