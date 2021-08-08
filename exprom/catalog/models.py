from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Pouf(models.Model):
    number = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.SET_DEFAULT)
    small_description = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.category} {self.number}'

    class Meta:
        verbose_name = 'Пуф'
        verbose_name_plural = 'Пуфы'


