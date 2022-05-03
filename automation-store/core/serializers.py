from rest_framework import serializers


class TShirtSerializer(serializers.Serializer):
    size = serializers.CharField(max_length=10)
    color = serializers.CharField(max_length=200)
    brand = serializers.CharField(max_length=200)
    price = serializers.FloatField()
