from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, PizzaViewSet

router = DefaultRouter()

router.register(r'restaurant', viewset=RestaurantViewSet, basename='api')
router.register(r'pizza', viewset=PizzaViewSet, basename='api')

urlpatterns = [

path('', include(router.urls))
]