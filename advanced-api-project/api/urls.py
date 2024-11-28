from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),  # ListView & CreateView
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # DetailView
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),  # CreateView
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),  # UpdateView
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # DeleteView
]