from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("create-book/", views.create_book),
    path("get-book/", views.get_book),
    path("update-book", views.update_book),
    path("delete-book", views.delete_book),
]
