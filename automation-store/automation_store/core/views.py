from automation_store.core.domain import Shirt
from automation_store.core.exceptions import (
    ApiShirtDoesNotExist,
    ServiceShirtDoesNotExistException,
)
from automation_store.core.serializers import (
    ShirtSerializer,
    ShirtUpdateSerializer,
)
from automation_store.core.services import ShirtService
from rest_framework import status, viewsets
from rest_framework.response import Response


# Create your views here.
class ShirtViewSet(viewsets.ViewSet):
    service = ShirtService()

    def create(self, request):
        serializer = ShirtSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.service.create(Shirt(**serializer.data))

        return Response([], status.HTTP_201_CREATED)

    def list(self, request):
        serializer = ShirtSerializer(self.service.list(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            shirt = self.service.get(pk)
            serializer = ShirtSerializer(shirt)

        except ServiceShirtDoesNotExistException:
            raise ApiShirtDoesNotExist()

        return Response(serializer.data, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = ShirtUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            shirt = self.service.update(id=pk, **serializer.data)
        except ServiceShirtDoesNotExistException:
            raise ApiShirtDoesNotExist()

        serializer = ShirtSerializer(shirt)
        return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            self.service.delete(pk)
        except ServiceShirtDoesNotExistException:
            raise ApiShirtDoesNotExist()

        return Response("", status.HTTP_200_OK)
