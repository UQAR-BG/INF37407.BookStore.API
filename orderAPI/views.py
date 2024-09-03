from rest_framework import generics

from .models import User, Book, Order
from .serializers import UserSerializer, BookSerializer, OrderSerializer

class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveDestroyUpdateUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"

class ListCreateBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveDestroyUpdateBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "isbn"

class ListCreateOrders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class RetrieveDestroyOrders(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    