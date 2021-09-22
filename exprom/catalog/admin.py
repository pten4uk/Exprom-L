from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('number',
              'slug',
              'category',
              'small_description',
              'description',
              ('width', 'height', 'depth'),
              'price'
              )