from django.urls import path
from .views import CreateUserView, provide_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # User-related URLs
    path('register/', CreateUserView.as_view(), name="register"),

    # Authentication URLs
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('lifetime/token/', provide_token, name='refresh_token'),
]
