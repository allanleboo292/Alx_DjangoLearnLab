from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
