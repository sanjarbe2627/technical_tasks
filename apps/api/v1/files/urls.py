from django.urls import path

from apps.api.v1.files import views

urlpatterns = [
    path("upload/", views.FileCreateView.as_view(), name="file-upload"),
    path("detail/<int:pk>/", views.FileDetailView.as_view(), name="file-detail"),
    path("download/<int:pk>/", views.FileDownloadView.as_view(), name="file-download")
]
