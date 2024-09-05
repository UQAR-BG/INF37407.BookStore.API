from rest_framework import generics

from .models import User, Book, Review
from .serializers import UserSerializer, BookSerializer, ReviewSerializer   

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUsers(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"

class ListBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveBooks(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "isbn"

class ListCreateReviews(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RetrieveDestroyReviews(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    