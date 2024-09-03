from rest_framework import serializers
from .models import User

class LoginSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ("email", "password")

class UserSerializer (serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ("id", "first_name", "last_name", "email", "password", "role")