from django.urls import include, path

from .views import CRMListView, CRMCreateView

app_name = 'crm'
urlpatterns = [
    path('list/', include([
        path('create/', CRMCreateView.as_view(), name='create'),
        path('', CRMListView.as_view(), name='list'),
    #     path('<int:id>/', PostDetailView.as_view(), name='detail'),
    #     path('<int:id>/edit/', PostUpdateView.as_view(), name='edit'),
        # path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    ])),
]
