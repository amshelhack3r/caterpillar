# pages/urls.py
from django.urls import path

from .views import hello

urlpatterns = [
    path('', hello.as_view(), name='home')
]
