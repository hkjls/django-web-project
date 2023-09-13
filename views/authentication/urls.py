from django.urls import path
from .views import pair_view, token_access
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/access/', token_access, name='token_list'),
    path('token/', pair_view.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]