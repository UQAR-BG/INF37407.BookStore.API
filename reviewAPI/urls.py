from django.urls import path

from .views import ListCreateUsers, RetrieveDestroyUpdateUsers, ListCreateBooks, RetrieveDestroyUpdateBooks, ListCreateReviews, RetrieveDestroyReviews

urlpatterns = [
    path("users/", ListCreateUsers.as_view(), name="ListCreateUsers"),
    path("users/<str:email>", RetrieveDestroyUpdateUsers.as_view(), name="RetrieveDestroyUpdateUsers"),
    path("books/", ListCreateBooks.as_view(), name="ListCreateBooks"),
    path("books/<str:isbn>", RetrieveDestroyUpdateBooks.as_view(), name="RetrieveDestroyUpdateBooks"),
    path("", ListCreateReviews.as_view(), name="ListCreateReviews"),
    path("<int:pk>", RetrieveDestroyReviews.as_view(), name="RetrieveDestroyReviews")
]