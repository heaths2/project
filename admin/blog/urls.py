from django.urls import include, path
from rest_framework import routers

from . import views
<<<<<<< HEAD
from .views import PostListView
=======
>>>>>>> d4a820d54a6a253e97bdaa67545bf699152a3d38

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
<<<<<<< HEAD
    path('blog/list', PostListView.as_view())
=======
    path('post/list', views.list),
>>>>>>> d4a820d54a6a253e97bdaa67545bf699152a3d38
]
# urlpatterns = [
#     path('<page_slug>-<page_id>/', include([
#         path('history/', views.history),
#         path('edit/', views.edit),
#         path('discuss/', views.discuss),
#         path('permissions/', views.permissions),
#     ])),
# ]