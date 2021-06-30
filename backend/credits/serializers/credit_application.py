""" Credit application serializer. """

# REST Framework
from rest_framework import serializers

# Models
from ..models import CreditApplication

class CreditApplicationModelSerializer(serializers.ModelSerializer):
    """ Credit Application serializer. """

    ai_indicator = serializers.IntegerField()

    class Meta:
        """ Meta class"""
        model = Credit
        fields = ['ai_indicator']
