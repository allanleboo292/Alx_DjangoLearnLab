from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_books, name='search_books'),
]
from django.urls import path
from .views import example_form_view

urlpatterns = [
    path("example-form/", example_form_view, name="example_form"),
]
