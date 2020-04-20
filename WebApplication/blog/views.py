from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import (
    FormView, CreateView, UpdateView, DeleteView
)
from rest_framework import viewsets, permissions

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

    class Meta:
        get_latest_by = ['create_at']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['author', 'title', 'content', 'image', 'files']
    template_name = ''
    success_url = '/'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['author', 'title', 'content', 'image', 'files']
    template_name = ''
    template_name_suffix = '_update_form'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # success_url = reverse_lazy('author-list')
    success_url = '/'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
