from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from coreApp.permissions import IsAdministrator
from .models import User, Book, Review
from .serializers import UserSerializer, BookSerializer, ReviewSerializer   

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]

class RetrieveUsers(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"
    permission_classes = [IsAuthenticated, IsAdministrator]

class ListBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class RetrieveBooks(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "isbn"
    permission_classes = [IsAuthenticated]

class ListCreateReviews(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class RetrieveDestroyReviews(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    