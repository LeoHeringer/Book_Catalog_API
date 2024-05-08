from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("/create-book", views.create_book),
    path("/get-book", views.get_book),
]
