from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

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
# views.py
# views.py
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter  # Import OrderingFilter
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains', label='Title')  # Case-insensitive title search
    author = filters.CharFilter(lookup_expr='icontains', label='Author')  # Case-insensitive author search
    publication_year = filters.NumberFilter(lookup_expr='exact', label='Publication Year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book with filtering, searching, and ordering options.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # Ensure OrderingFilter is included
    filterset_class = BookFilter  # Apply custom filter set to this view
    filters.SearchFilter= ['title', 'author']  # Allow searching by title and author
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and publication year
    filters.OrderingFilter= ['title']  # Default ordering by title
