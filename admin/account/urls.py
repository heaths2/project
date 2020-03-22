from django.urls import path

from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),/
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
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