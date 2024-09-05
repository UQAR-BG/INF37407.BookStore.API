from rest_framework import generics

from .models import User, Book, Recommendation
from .serializers import UserSerializer, BookSerializer, RecommendationSerializer

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

class ListCreateRecommendations(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class RetrieveDestroyRecommendations(generics.RetrieveDestroyAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    