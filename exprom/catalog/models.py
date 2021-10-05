import os

from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .utils import upload_function


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    number = models.PositiveSmallIntegerField('Номер', primary_key=True)
    slug = models.SlugField(
        'Имя ссылки',
        help_text='Подсказка: введите название товара английскими буквами, заменяя пробелы нижними подчеркиваниями.'
                  ' Пример: kvadratniy_pouf',
        max_length=30,
        unique=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        null=True,
        default=None,
        on_delete=models.SET_DEFAULT,
    )
    photo = models.ImageField('Главное фото', upload_to=upload_function, null=True, blank=True)
    small_description = models.CharField('Краткое описание', max_length=250, blank=True)
    description = models.TextField('Описание', blank=True)
    width = models.PositiveSmallIntegerField('Ширина')
    height = models.PositiveSmallIntegerField('Высота')
    depth = models.PositiveSmallIntegerField('Глубина')
    price = models.PositiveSmallIntegerField('Цена', default=0)

    def __str__(self):
        return f'{self.category} {self.number}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['number']


class Photo(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    photo = models.ImageField('Изображение', upload_to=upload_function)

    def __str__(self):
        return f'Изображение {self.pk} для {self.content_object}'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
