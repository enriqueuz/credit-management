""" Authentication views. """

# Django
from django.contrib.auth import authenticate, login, logout

# REST Framework
from rest_framework import status, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from .serializers import UserSerializer

class LoginView(APIView):
    """ Login view. """
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    """ Logout view. """
    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)


class SignupView(generics.CreateAPIView):
    """ Sign up view. """
    serializer_class = UserSerializer