from rest_framework import generics

from .models import User, Book, Recommendation
from .serializers import UserSerializer, BookSerializer, RecommendationSerializer

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

class ListCreateRecommendations(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class RetrieveDestroyRecommendations(generics.RetrieveDestroyAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    