from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("create/", views.create, name="create"),
    path("random/", views.random, name="random"),
    path("edit/", views.edit, name="edit"),
    path("editing/", views.editing, name="editing"),
    path("search/", views.search, name="search"),
]
