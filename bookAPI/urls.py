from django.urls import path

from .views import ListCreateBooks, RetrieveUpdateDestroyBooks

urlpatterns = [
    path("", ListCreateBooks.as_view(), name="ListCreateBooks"),
    path("<str:isbn>", RetrieveUpdateDestroyBooks.as_view(), name="RetrieveUpdateDestroyBooks")
]