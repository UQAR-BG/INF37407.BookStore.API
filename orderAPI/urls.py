from django.urls import path

from .views import ListCreateUsers, RetrieveDestroyUpdateUsers

urlpatterns = [
    path("users/", ListCreateUsers.as_view(), name="ListCreateUsers"),
    path("users/<int:id>", RetrieveDestroyUpdateUsers.as_view(), name="RetrieveDestroyUpdateUsers")
]