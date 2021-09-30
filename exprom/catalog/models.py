from django.contrib import admin
from django.db import models

from .utils import photo_directory_path


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
    photos = models.OneToOneField('Photo', on_delete=models.CASCADE, null=True, related_name='photos')
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
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    general_photo = models.ImageField('Главная фотография', null=True, blank=True, upload_to=photo_directory_path)
    second_photo = models.ImageField('Дополнительное фото 1', null=True, blank=True, upload_to=photo_directory_path)
    third_photo = models.ImageField('Дополнительное фото 2', null=True, blank=True, upload_to=photo_directory_path)

    def __str__(self):
        return f'{self.product.category} {self.product.number}'
