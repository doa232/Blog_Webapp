from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),  # function base view
    path('', PostListView.as_view(), name='blog-home'),  # class base view
    path('user/<str:username>', UserPostListView.as_view(),
         name='user-posts'),  # class base view
    path('post/<int:pk>/', PostDetailView.as_view(),
         name='post-detail'),  # class base view
    path('post/new/', PostCreateView.as_view(),
         name='post-create'),  # class base view
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post-update'),  # class base view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post-delete'),  # class base view
    path('about/', views.about, name='blog-about'),

]
