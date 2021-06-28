from django.shortcuts import render
from .models import Restaurant, Pizza
from .serializers import RestaurantSerializer, PizzaSerializer
# Create your views here.
from rest_framework import viewsets


class RestaurantViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer