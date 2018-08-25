from django.urls import path

from .views import ListView


urls = [
    path('', ListView.as_view()),
]
