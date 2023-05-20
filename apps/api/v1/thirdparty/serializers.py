from rest_framework import serializers


class ThirtyPartySerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100, required=True)
