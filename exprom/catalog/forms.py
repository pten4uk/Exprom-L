from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.contrib.flatpages.models import FlatPage

from .models import Product


class FlatpagesAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorWidget())

    class Meta:
        model = FlatPage
        fields = ('content',)
