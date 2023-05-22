import os
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse
from django.conf import settings

from apps.api.v1.files import serializers
from apps.files.models import File


# Task 7
class FileCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = serializers.FileSerializers
    permission_classes = (IsAuthenticated,)


class FileDetailView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = serializers.FileSerializers
    permission_classes = (IsAuthenticated,)


class FileDownloadView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        file = File.objects.filter(pk=kwargs['pk']).first()
        if file:
            file_path = f"{settings.MEDIA_ROOT}/{file.file.name}"
            if os.path.exists(file_path):
                file = open(file_path, 'rb')
                response = FileResponse(file)
                response['Content-Disposition'] = f'attachment; filename="{file.name}"'
                return response

        return Response({'error': 'File not found.'}, status=status.HTTP_404_NOT_FOUND)
