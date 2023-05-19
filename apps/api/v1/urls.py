from django.urls import path, include

from apps.api.v1.auth import urls as auth_urls

urlpatterns = [
    path('auth/', include(auth_urls))
]
