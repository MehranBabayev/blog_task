from django.urls import path
from .views import (
    BlogListAPIView,
    BlogDetailView,
    BlogUpdateView,
    BlogCommentAPIView,
    BlogCommentUpdateAPIView,
    LikeDislikeCreateView,
    CategoryListView,
    TagListView
)

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blog_list'),
    path('blogs/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/<slug:slug>/comments/', BlogCommentAPIView.as_view(), name='blog_comments'),
    path('blogs/<slug:slug>/comments/<int:pk>/', BlogCommentUpdateAPIView.as_view(), name='blog_comment_update'),
    path('comments/<int:pk>/like-dislike/', LikeDislikeCreateView.as_view(), name='comment_like_dislike'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
]
