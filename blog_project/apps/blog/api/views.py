from apps.blog.models import Blog, Blog_comment, LikeDislike, IPs, Category, Tag
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import (
    BlogSerializer,
    BlogCreateSerializer,
    BlogDetailSerializer,
    BlogCommentCreateSerializer,
    BlogCommentSerializer,
    LikeDislikeSerializer,
    CategorySerializer,
    TagSerializer
    )

from rest_framework.generics import  (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    CreateAPIView,
    ListAPIView
    )



class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogListAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.published.all()[:9]
    permission_classes = (IsAuthenticatedOrReadOnly, )
    parser_classes = (MultiPartParser,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogCreateSerializer
        return super().get_serializer_class() 


class BlogDetailView(RetrieveAPIView):
    queryset = Blog.published.all()
    serializer_class = BlogDetailSerializer

    def get(self, request, pk, format=None):
        blogs = get_object_or_404(Blog, pk=pk)
        ip = self.get_client_ip(request)
        ip_obj, created = IPs.objects.get_or_create(view_ip=ip)
        blogs.viewed_ips.add(ip_obj)
        serializer = BlogDetailSerializer(blogs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class BlogUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.published.all()
    serializer_class = BlogSerializer


class BlogCommentAPIView(CreateAPIView):
    serializer_class = BlogCommentCreateSerializer


class BlogCommentUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog_comment.published.all()
    serializer_class = BlogCommentSerializer
    
    
class LikeDislikeCreateView(CreateAPIView):
    serializer_class = LikeDislikeSerializer
    queryset = LikeDislike.objects.all()


    def perform_create(self, serializer):
        user = self.request.user
        comment_id = self.request.data.get('comment')
        comment = Blog_comment.objects.get(pk=comment_id)
        action = self.request.data.get('action')


        existing_action = LikeDislike.objects.filter(user=user, comment=comment).first()
        if not existing_action:
            serializer.save(user=user, comment=comment, action=action)
        else:
            existing_action.action = action
            existing_action.save()
