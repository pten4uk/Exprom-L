from django.contrib import admin
from .models import *

admin.site.site_title = 'Администрирование Экспром-Л'
admin.site.site_header = 'Администрирование Экспром-Л'


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
    list_display = ('get_str_title', 'small_description', 'price')
    fields = ('number',
              'slug',
              'category',
              'photos',
              'small_description',
              'description',
              ('width', 'height', 'depth'),
              'price'
              )
    list_filter = ('category',)
    change_form_template = 'admin/change_form.html'

    def get_str_title(self, obj):
        return f'{obj.category} {obj.number}'
    get_str_title.short_description = 'Название'


    def save_model(self, request, obj, form, change):
        print(obj.photos.get(pk=1))
        return super().save_model(request, obj, form, change)