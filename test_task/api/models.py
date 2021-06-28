from django.db import models
from utils.constants import CHEESE_TYPE_CHOICES, DOUGH_T_TYPE_CHOICES

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

class Pizza(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    cheese_type = models.CharField(max_length=20, choices=CHEESE_TYPE_CHOICES, default='Моцарелла', verbose_name='Вид Сыра')
    dough_thickness = models.CharField(max_length=20, choices=DOUGH_T_TYPE_CHOICES, default='Тонкое тесто', verbose_name='Толщина Теста')
    secret_ingredient = models.CharField(max_length=255, null=True, blank=True, verbose_name='Секретный Ингредиент')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT, verbose_name='Ресторан', null=True)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'