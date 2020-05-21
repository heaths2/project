from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, DeleteView, CreateView, UpdateView
)
from rest_framework import viewsets, permissions

from .forms import PostForm
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


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
    template_name = 'blog/DD.html'
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
    template_name = 'blog/Edit.html'

    login_url = 'sso/Login'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        return super(PostCreateView, self).form_valid(form)

    # def get_success_url(self):
    #     return '/'

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['author', 'status', 'title', 'content', 'image', 'files']
    # form_class = 'PostForm'
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
    # success_url = reverse_lazy('author-list')
    login_url = 'sso/login'
    success_url = 'blog:list'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def post_list(request):
    posts = Post.objects.filter(
        create_at__lte=timezone.now()).order_by('-create_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def add_comment_to_post(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/add_comment_to_post.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
