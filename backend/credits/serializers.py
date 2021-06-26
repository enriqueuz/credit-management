""" Authentication serializers. """

# REST Framework
from django.db.models import fields
from rest_framework import serializers

# Models
from .models import Credit, Client, CreditApplication

class CreditSerializer(serializers.ModelSerializer):
    """ Credit Serializer """
    client = ClientSerializer()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Credit
        fields = ['amount']
    
    def create(self, validated_data):

class ClientSerializer(serializers.ModelSerializer):

    """ Client serilizer """

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    sbs_debt = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Client
        fields = '__all__'