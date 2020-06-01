from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.urls import reverse_lazy
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, DeleteView, CreateView, UpdateView
)
import logging
# This retrieves a Python logging instance (or creates it)

from rest_framework import viewsets, permissions

from .forms import PostForm
from .models import Post, Comment
from user.models import User
from .serializers import PostSerializer, CommentSerializer

logger = logging.getLogger(__name__)


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'blog/List.html'
    # template_name = 'blog/post_list.html'
    queryset = Post.objects.all()
    # queryset = Post.objects.all().order_by('-created_at')[:10]
    ordering = ['-created_at']
    # paginate_by = 10
    login_url = 'sso/Login'
    resolve_url = 'user:Login'

    # print(queryset)


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blog/Detail.html'
    # form_class = PostForm
    # queryset = Post.objects.filter(id__gt=1)
    login_url = 'sso/Login'

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Post, pk=_id)

    def get_context_data(self, **kwargs):
        # 생성된 context는 Template으로 전달됨.
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm(self.request)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    # model = Post
    # fields = ['author', 'status', 'title', 'content', 'image', 'files']    
    template_name = 'blog/Create.html'

    login_url = 'sso/Login'
    success_url = reverse_lazy('blog:list')

    pk_url_kwargs = 'post_id'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        article = queryset.filter(pk=pk).first()

        if pk:
          if not article:
            raise Http404('invalid pk')
          elif article.author != self.request.user:  # 작성자가 수정하려는 사용자와 다른 경우
            raise Http404('invalid user')
        return article

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        queryset = Post.objects.filter(post__author=self.request.session.get('user'))
        return super(PostCreateView, self).form_valid(form)

    # def get_success_url(self):
    #     return '/'

    # def get_context_data(self, **kwargs):
    #     # 생성된 context는 Template으로 전달됨.
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = PostForm(self.request)
    #     return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    template_name = 'blog/Edit.html'
    login_url = 'sso/login'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Post, pk=_id)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # template_name = 'blog/Confirm_Delete.html'
    # success_url = reverse_lazy('author-list')
    login_url = 'sso/login'
    success_url = 'blog:list'

    # def get_object(self):
    #     _id = self.kwargs.get("id")
    #     return get_object_or_404(Post, pk=_id)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
