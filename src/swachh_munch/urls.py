"""swachh_munch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from pages.views import home_page
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

urlpatterns = [
    path('', home_page, name='home'),
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls),
    path('api/users/', include('profiles.api.urls', namespace="api-profiles")),
    path('api/channels/', include('basic.api.urls', namespace="api-channels")),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token)
]
