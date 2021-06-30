""" Authentication urls. """

# Django
from django.urls import path

# REST Framework
from rest_framework.authtoken.views import obtain_auth_token

# Views
from .views import SignupView

urlpatterns = [
    path('auth/signup/', SignupView.as_view(), name='auth_signup'),
    path('auth/token-auth/', obtain_auth_token, name='api_token_auth'),
]