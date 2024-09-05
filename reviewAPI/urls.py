from django.urls import path

from .views import ListUsers, RetrieveUsers, ListBooks, RetrieveBooks, ListCreateReviews, RetrieveDestroyReviews

urlpatterns = [
    path("users/", ListUsers.as_view(), name="ListUsers"),
    path("users/<str:email>", RetrieveUsers.as_view(), name="RetrieveUsers"),
    path("books/", ListBooks.as_view(), name="ListBooks"),
    path("books/<str:isbn>", RetrieveBooks.as_view(), name="RetrieveBooks"),
    path("", ListCreateReviews.as_view(), name="ListCreateReviews"),
    path("<int:pk>", RetrieveDestroyReviews.as_view(), name="RetrieveDestroyReviews")
]