from django.urls import path

from .views.place import ListView


urls = [
    path('', ListView.as_view()),
]
