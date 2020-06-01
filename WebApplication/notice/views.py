from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, DeleteView, CreateView, UpdateView
)

from .models import Post
from .forms import PostForm


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'notice/List.html'
    queryset = Post.objects.all()
    # queryset = Post.objects.all().order_by('-created_at')[:10]
    ordering = ['-created_at']
    # paginate_by = 10
    login_url = 'sso/Login'
    resolve_url = 'user:Login'


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'notice/Detail.html'
    # form_class = PostForm
    # context_object_name = 'form'
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
    template_name = 'notice/Create.html'
    login_url = 'sso/Login'
    success_url = reverse_lazy('notice:list')

    def form_valid(self, form):
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    template_name = 'notice/Edit.html'
    login_url = 'sso/login'
    success_url = reverse_lazy('notice:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Post, pk=_id)

    # def get_object(self):
    #     return get_object_or_404(Post, pk=self.kwargs['id'])

    # def get_object(self):
    #     return self.request.user


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'notice/Confirm_Delete.html'
    # form_class = PostForm

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Post, pk=_id)

    def get_success_url(self):
        return reverse('notice:list')
