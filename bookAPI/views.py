from rest_framework import generics, status
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Book
from .serializers import BookSerializer

class ListCreateBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('genre', openapi.IN_QUERY, description="Genre of book", type=openapi.TYPE_STRING),
            openapi.Parameter('author', openapi.IN_QUERY, description="Author of book", type=openapi.TYPE_STRING),
            openapi.Parameter('title', openapi.IN_QUERY, description="Title of book", type=openapi.TYPE_STRING),
            openapi.Parameter('isbn', openapi.IN_QUERY, description="ISBN of book", type=openapi.TYPE_STRING)
        ],
    )
    def get(self, request):
        genre = request.query_params.get('genre', None)
        author = request.query_params.get('author', None)
        title = request.query_params.get('title', None)
        isbn = request.query_params.get('isbn', None)

        books = Book.objects.all()
        if genre:
            books = books.filter(genre__icontains=genre)
        if author:
            books = books.filter(author__icontains=author)
        if title:
            books = books.filter(title__icontains=title)
        if isbn:
            books = books.filter(isbn__icontains=isbn)
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateDestroyBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "isbn"