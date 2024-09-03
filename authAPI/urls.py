from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import login, signUp, logout, me

schema_view = get_schema_view(
    openapi.Info(
        title="Authentification API",
        default_version="v1.0",
        description="Book store application'",
    ),
    public=True,
)

urlpatterns = [
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('signUp', signUp, name="signUp" ),
    path('me', me, name="me"),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

