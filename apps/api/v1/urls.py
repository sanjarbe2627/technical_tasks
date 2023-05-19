from django.urls import path, include

from apps.api.v1.auth import urls as auth_urls
from apps.api.v1.sponsor import urls as sponsor_urls

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('sponsor/', include(sponsor_urls)),
]
