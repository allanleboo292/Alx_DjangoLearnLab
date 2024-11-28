from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users only

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users only

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    """
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Restrict to authenticated users only
