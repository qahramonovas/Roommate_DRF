from apps.views import RegisterUserCreateAPIView, CodeUserAPIView, SendEmailAPIView
from django.urls import path

urlpatterns = [
    path('auth/register', RegisterUserCreateAPIView.as_view()),
    path('auth/send/verify', CodeUserAPIView.as_view()),
    path('auth/send/mail', SendEmailAPIView.as_view()),
]
