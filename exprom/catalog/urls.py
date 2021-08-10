from django.urls import path
from .views import PoufList, PoufDetail


urlpatterns = [
    path('', PoufList.as_view()),
    path('<pk>', PoufDetail.as_view()),
]
