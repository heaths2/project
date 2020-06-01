from django.urls import include, path
from rest_framework import routers

from . import views
from .views import (
    PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
)

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)

app_name = 'blog'
urlpatterns = [
    path('', include(router.urls)),
    path('list/', include([
        path('', PostListView.as_view(), name='list'),
        path('create/', PostCreateView.as_view(), name='create'),
        path('<int:id>/', PostDetailView.as_view(), name='detail'),
        path('<int:id>/edit/', PostUpdateView.as_view(), name='edit'),
        path('<int:id>/delete/', PostDeleteView.as_view(), name='delete'),
    ])),
]
