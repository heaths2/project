from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets, permissions

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListView(ListView):
    model = Post
    paginate_by = 10

    class Meta:
        get_latest_by = ['create_at']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]