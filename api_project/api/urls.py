# api/urls.py
from django.urls import path
from .views import BookList  # Import your view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Map '/books/' to the BookList view
]
