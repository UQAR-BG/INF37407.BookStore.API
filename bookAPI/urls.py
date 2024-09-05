from django.urls import path

from .views import ListBooks, CreateBooks, RetrieveUpdateDestroyBooks

urlpatterns = [
    path("", ListBooks.as_view(), name="ListBooks"),
    path("<str:isbn>", RetrieveUpdateDestroyBooks.as_view(), name="RetrieveUpdateDestroyBooks"),
    path("create/", CreateBooks.as_view(), name="CreateBooks"),
]