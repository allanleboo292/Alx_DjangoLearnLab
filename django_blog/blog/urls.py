# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),  # Ensure this exists
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Ensure this exists
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Ensure this exists
]


