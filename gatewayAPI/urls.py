"""
URL configuration for gatewayAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Book store API",
        default_version="v1.0",
        description="Book store app'",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authAPI.urls')),
    path('book/', include('bookAPI.urls')),
    path('order/', include('orderAPI.urls')),
    path('review/', include('reviewAPI.urls')),
    path('recommendation/', include('recommendationAPI.urls')),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
