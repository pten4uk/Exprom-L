import os

from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *

admin.site.site_title = 'Администрирование Экспром-Л'
admin.site.site_header = 'Администрирование Экспром-Л'


class PhotoInline(GenericTabularInline):
    model = Photo
    verbose_name = 'Дополнительное фото'
    verbose_name_plural = 'Дополнительные фото'
    extra = 0

    def get_queryset(self, request):
        qs = super().get_queryset(request).prefetch_related('content_object', 'content_type')
        pks = []
        for image in qs:
            if image.photo and not os.path.exists(image.photo.path):
                pks.append(image.pk)
        Photo.objects.filter(pk__in=pks).delete()
        qs = qs.exclude(pk__in=pks)
        return qs


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_select_related = True
    list_display = ('get_str_title', 'small_description', 'price')
    fields = ('number',
              'slug',
              'category',
              'photo',
              'small_description',
              'description',
              ('width', 'height', 'depth'),
              'price'
              )
    list_filter = ('category',)

    def get_str_title(self, obj):
        return f'{obj.category} {obj.number}'
    get_str_title.short_description = 'Название'

    def get_object(self, request, object_id, from_field=None):
        object = Product.objects.select_related('category').get(pk=object_id)
        if object.photo and not os.path.exists(object.photo.path):
            object.photo = None
        return object


# -------------------------------------------------Developer Mode-------------------------------------------------------


if settings.DEBUG:

    admin.site.register(Photo)

    admin.site.site_title = 'Администрирование в режиме разработки'
    admin.site.site_header = 'Администрирование в режиме разработки'
