# api/urls.py
from django.urls import path, include
from .views import BookList, BookViewSet  # Import your view
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

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
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    # other endpoints
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
