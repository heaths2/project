from django.urls import include, path

from .views import (
    PostListView, PostCreateView, PostDetailView, PostUpdateView,
    # , PostDetailView, PostUpdateView, PostDeleteView
)

app_name = 'notice'
urlpatterns = [
    path('list/', include([
        path('', PostListView.as_view(), name='list'),
        path('create/', PostCreateView.as_view(), name='create'),
        path('<int:id>/', PostDetailView.as_view(), name='detail'),
        path('<int:id>/edit/', PostUpdateView.as_view(), name='edit'),
        # path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    ])),
]
