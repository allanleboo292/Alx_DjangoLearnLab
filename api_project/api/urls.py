# api/urls.py
from django.urls import path
from .views import BookList, BookViewSet  # Import your view
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Map '/books/' to the BookList view
]
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename="book_all")
urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]