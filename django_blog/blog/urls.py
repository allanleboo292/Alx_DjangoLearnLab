# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView,CommentUpdateView,CommentDeleteView
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
    path('post/<int:post_id>/comment/new/', views.add_comment, name='add-comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),
    path('post/<int:post_id>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
     path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]


