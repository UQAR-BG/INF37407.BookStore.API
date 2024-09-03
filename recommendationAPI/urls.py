from django.urls import path

from .views import ListCreateUsers, RetrieveDestroyUpdateUsers, ListCreateBooks, RetrieveDestroyUpdateBooks, ListCreateRecommendations, RetrieveDestroyRecommendations

urlpatterns = [
    path("users/", ListCreateUsers.as_view(), name="ListCreateUsers"),
    path("users/<str:email>", RetrieveDestroyUpdateUsers.as_view(), name="RetrieveDestroyUpdateUsers"),
    path("books/", ListCreateBooks.as_view(), name="ListCreateBooks"),
    path("books/<str:isbn>", RetrieveDestroyUpdateBooks.as_view(), name="RetrieveDestroyUpdateBooks"),
    path("", ListCreateRecommendations.as_view(), name="ListCreateRecommendations"),
    path("<int:pk>", RetrieveDestroyRecommendations.as_view(), name="RetrieveDestroyRecommendations")
]