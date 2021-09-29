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
    list_filter = ('category',)
    fieldsets = (
        (None, {'fields': ('number',)}),
        (None, {'fields': ('slug',)}),
        (None, {'fields': ('category',)}),
        (None, {'fields': ('small_description',)}),
        (None, {'fields': ('description',)}),
        (None, {'fields': ('width', 'height', 'depth')}),
        (None, {'fields': ('price',)}),
              )

    def save_model(self, request, obj, form, change):
        print(obj, form, change)
        return super().save_model(request, obj, form, change)
