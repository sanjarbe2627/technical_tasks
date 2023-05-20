import requests
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _

from apps.api.v1.thirdparty import serializers


# Task 9
class ThirtyWeatherView(generics.GenericAPIView):
    serializer_class = serializers.ThirtyPartySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city = serializer.validated_data.get('city')
        api_key = "5ad0c49c2c57439c970c433802dbfdcd"

        url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": 'Error occurred while fetching weather data'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
