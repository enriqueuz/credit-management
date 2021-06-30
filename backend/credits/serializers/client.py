""" Client serializers. """

# REST Framework
from rest_framework import serializers

# Models
from ..models import Client

class ClientModelSerializer(serializers.ModelSerializer):
    """ Client serilizer """

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    sbs_debt = serializers.DecimalField(max_digits=10, decimal_places=2)
    debtor_score = serializers.CharField(max_length=7)

    class Meta:
        """ Meta class"""
        model = Client
        fields = '__all__'