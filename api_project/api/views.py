from django.shortcuts import render

from rest_framework import generics
from .serializers import BookSerializer
from .models import Book  # Import the Book model
from rest_framework.viewsets import ModelViewSet
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data
class BookViewSet(ModelViewSet):
    queryset = user.object.all()
    serializer_class = BookSerializer
