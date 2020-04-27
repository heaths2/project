from django.urls import include, path
from rest_framework import routers
# from django.contrib.auth import views as auth_views

# from .views import RegisterView, LogoutView
from .views import RegisterView, LoginView, LogoutView

from . import views

router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)

app_name = 'user'
urlpatterns = [
    # path('Login/', auth_views.LoginView.as_view(template_name='account/Login.html'), name="Login"),
    path('SignUp/', RegisterView.as_view(), name="SignUp"),
    path('Login/', LoginView.as_view(), name="Login"),
    path('Logout/', LogoutView.as_view(), name="Logout"),
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
