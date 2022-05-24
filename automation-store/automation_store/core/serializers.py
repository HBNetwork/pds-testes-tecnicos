from rest_framework import serializers


class ShirtSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    size = serializers.CharField()
    color = serializers.CharField(max_length=200)
    brand = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=None, decimal_places=2)
    slug = serializers.CharField(max_length=200, required=False)
