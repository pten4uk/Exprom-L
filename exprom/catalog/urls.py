from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductList.as_view(), name='catalog'),
    path('<pk>', ProductDetail.as_view(), name='product'),
]
