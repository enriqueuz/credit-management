""" Credits views. """

# REST Framework
from django.db import models
from rest_framework import status, viewsets

# Models
from .models import Credit

# Serializer
from .serializers import CreditModelSerializer

class CreditModelViewSet(viewsets.ModelViewSet):
    """ Credits model viewset. """

    queryset = Credit.objects.all()
    serializer_class = CreditModelSerializer


