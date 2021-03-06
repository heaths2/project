from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import (
    RegisterView, LoginView, LogoutView, RegisterAPI, LoginAPI, UserAPI,
)

from . import views

router = routers.DefaultRouter()
router.register(r'user', views.AccountViewSet)

app_name = 'user'
urlpatterns = [
    path('', include(router.urls)),
    # path('Login/', auth_views.LoginView.as_view(template_name='account/Login.html'), name="Login"),
    path('SignUp/', RegisterView.as_view(), name="SignUp"),
    path('Login/', LoginView.as_view(), name="Login"),
    path('Logout/', LogoutView.as_view(), name="Logout"),
    path(
        'jwt/', include([
            path('token/', TokenObtainPairView.as_view(),
                 name='token_obtain_pair'),
            path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            path('verify/', TokenVerifyView.as_view(), name='token_verify'),
        ])),
    path('ssosign/', RegisterAPI.as_view(), name="ssosign"),
    path('ssoin/', LoginAPI.as_view(), name="ssoin"),
    path('ssoout/', UserAPI.as_view(), name="ssoout"),
]
