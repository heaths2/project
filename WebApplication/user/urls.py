from django.urls import include, path
from rest_framework import routers

from .views import RegisterView, LoginView, LogoutView
from . import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),/
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('', include('user.urls')),
]
# urlpatterns = [
#     path('<page_slug>-<page_id>/', include([
#         path('history/', views.history),
#         path('edit/', views.edit),
#         path('discuss/', views.discuss),
#         path('permissions/', views.permissions),
#     ])),
# ]