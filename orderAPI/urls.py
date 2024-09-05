from django.urls import path

from .views import ListUsers, RetrieveUsers, ListBooks, RetrieveBooks, ListCreateOrders, RetrieveDestroyOrders

urlpatterns = [
    path("users/", ListUsers.as_view(), name="ListUsers"),
    path("users/<str:email>", RetrieveUsers.as_view(), name="RetrieveUsers"),
    path("books/", ListBooks.as_view(), name="ListBooks"),
    path("books/<str:isbn>", RetrieveBooks.as_view(), name="RetrieveBooks"),
    path("", ListCreateOrders.as_view(), name="ListCreateOrders"),
    path("<int:pk>", RetrieveDestroyOrders.as_view(), name="RetrieveDestroyOrders")
]