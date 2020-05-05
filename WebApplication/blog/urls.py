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
    path('edit/', PostUpdateView.as_view(), name='edit'),
    path('list/', include([
        path('', PostListView.as_view(), name='list'),
        path('<int:pk>', PostDetailView.as_view(), name='detail'),
        path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    ])),
]
