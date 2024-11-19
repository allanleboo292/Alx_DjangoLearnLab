from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library

from django.shortcuts import render
from .models import Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Library


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books') 
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def check_role(role):
    def decorator(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
