from django.urls import path

from .views import ListCreateUsers, RetrieveDestroyUpdateUsers, ListCreateBooks, RetrieveDestroyUpdateBooks, ListCreateOrders, RetrieveDestroyOrders

urlpatterns = [
    path("users/", ListCreateUsers.as_view(), name="ListCreateUsers"),
    path("users/<str:email>", RetrieveDestroyUpdateUsers.as_view(), name="RetrieveDestroyUpdateUsers"),
    path("books/", ListCreateBooks.as_view(), name="ListCreateBooks"),
    path("books/<str:isbn>", RetrieveDestroyUpdateBooks.as_view(), name="RetrieveDestroyUpdateBooks"),
    path("", ListCreateOrders.as_view(), name="ListCreateOrders"),
    path("<int:pk>", RetrieveDestroyOrders.as_view(), name="RetrieveDestroyOrders")
]