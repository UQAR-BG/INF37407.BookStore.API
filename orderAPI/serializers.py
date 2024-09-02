from rest_framework import serializers

from .models import User, Order, Book, BookLine

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]

class BookLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLine

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order