from rest_framework import serializers


class ShirtSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    size = serializers.CharField(max_length=10)
    color = serializers.CharField(max_length=200)
    brand = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    slug = serializers.CharField(max_length=200, required=False)
