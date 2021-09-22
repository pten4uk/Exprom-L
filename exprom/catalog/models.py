from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    number = models.PositiveSmallIntegerField('Номер', primary_key=True)
    category = models.ForeignKey(Category, verbose_name='Категория', null=True, default=None, on_delete=models.SET_DEFAULT)
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


