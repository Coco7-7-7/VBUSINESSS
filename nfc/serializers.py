from rest_framework import serializers
from .models import NFCTag, CustomUser


class NFCTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFCTag
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
