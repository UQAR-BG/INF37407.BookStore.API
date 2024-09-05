from django.urls import path

from .views import ListUsers, RetrieveUsers, ListBooks, RetrieveBooks, ListCreateRecommendations, RetrieveDestroyRecommendations

urlpatterns = [
    path("users/", ListUsers.as_view(), name="ListUsers"),
    path("users/<str:email>", RetrieveUsers.as_view(), name="RetrieveUsers"),
    path("books/", ListBooks.as_view(), name="ListBooks"),
    path("books/<str:isbn>", RetrieveBooks.as_view(), name="RetrieveBooks"),
    path("", ListCreateRecommendations.as_view(), name="ListCreateRecommendations"),
    path("<int:pk>", RetrieveDestroyRecommendations.as_view(), name="RetrieveDestroyRecommendations")
]