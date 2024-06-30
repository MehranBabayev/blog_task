from django.urls import path
from .views import RegistrationAPIView, ActivateAccountView, LoginAPIView, LogoutAPIView, ProfileDetailAPIView, PasswordResetAPIView, PasswordResetConfirmAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('activate/', ActivateAccountView.as_view(), name='activate'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('profile/', ProfileDetailAPIView.as_view(), name='profile'),
    path('password_reset/', PasswordResetAPIView.as_view(), name='password_reset'),
    path('password_reset_confirm/', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
]