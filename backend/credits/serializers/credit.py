""" Authentication serializers. """

# REST Framework
from django.db import models
from django.db.models import fields
from rest_framework import serializers

# Models
from ..models import Credit, Client, CreditApplication

# Serializers
from .client import ClientModelSerializer
from .credit_application import CreditApplicationModelSerializer

# Utils
from collections import OrderedDict

class CreditModelSerializer(serializers.ModelSerializer):
    """ Credit Serializer """
    client = ClientModelSerializer()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    ai_indicator = serializers.ChoiceField(
        choices=CreditApplication.AI_INDICATOR_CHOICES,
        write_only=True
        )

    class Meta:
        """ Meta class"""
        model = Credit
        fields = ['amount', 'pending_approval', 'client', 'ai_indicator', 'application_ai_ind']

    def create(self, validated_data):
        """ Create credit and client. """

        client = Client.objects.create(**validated_data['client'])

        instance = Credit.objects.create(
            amount=validated_data['amount'], 
            client=client)
                    
        CreditApplication.objects.create(
            ai_indicator=validated_data['ai_indicator'],
            credit=instance
        )
        
        return instance
    
    def to_representation(self, instance):
        """ Change 'application_ai_ind' to 'application_ai_ind' """

        ret = super().to_representation(instance)

        if 'application_ai_ind' in ret:
            ret = OrderedDict(
                ('ai_indicator' 
                if k == 'application_ai_ind' 
                else k, v) 
                for k, v in ret.items()
                )

        return ret