""" Authentication views. """

# Django
from django.contrib.auth import authenticate, login, logout

# REST Framework
from rest_framework import status, generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from .serializers import UserSerializer

class SignupView(generics.CreateAPIView):
    """ Sign up view. """
    permission_classes = [permissions.AllowAny]
    
    serializer_class = UserSerializer