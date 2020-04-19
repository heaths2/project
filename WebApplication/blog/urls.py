from django.urls import include, path
from rest_framework import routers

from . import views
from .views import PostListView

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)

app_name = 'blog'
urlpatterns = [
    path('', include(router.urls)),
    path('list/', PostListView.as_view(), name='list')
]
# urlpatterns = [
#     path('<page_slug>-<page_id>/', include([
#         path('history/', views.history),
#         path('edit/', views.edit),
#         path('discuss/', views.discuss),
#         path('permissions/', views.permissions),
#     ])),
# ]
