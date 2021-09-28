from django.contrib import admin
from .models import *


class PhotoInline(admin.TabularInline):
    model = Photo
    verbose_name = 'Фото'
    verbose_name_plural = 'Фото'
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    fields = ('number',
              'slug',
              'category',
              'small_description',
              'description',
              ('width', 'height', 'depth'),
              'price'
              )
    list_filter = ('category',)
