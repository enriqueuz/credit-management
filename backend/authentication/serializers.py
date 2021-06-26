""" Authentication serializers. """

# REST Framework
from rest_framework import serializers

# Django
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """ User serializer. """
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def create(self, validated_data):
        """ Manage user creation. """

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
    

    def validate_username(self, value):
        """ Check user doest not exists"""
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("El usuario ya existe")
        
        return value