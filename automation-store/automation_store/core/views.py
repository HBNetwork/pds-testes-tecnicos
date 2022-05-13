from automation_store.core.domain import Shirt
from automation_store.core.exceptions import ServiceResourceDoesNotExistException
from automation_store.core.serializers import ShirtSerializer
from automation_store.core.services import ShirtService
from rest_framework import status, viewsets
from rest_framework.response import Response


# Create your views here.
class ShirtViewSet(viewsets.ViewSet):
    service = ShirtService()

    def create(self, request):
        serializer = ShirtSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.service.create(Shirt(**serializer.data))

        return Response([], status.HTTP_201_CREATED)

    def list(self, request):
        serializer = ShirtSerializer(self.service.list(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            shirt = self.service.get(pk)
            serializer = ShirtSerializer(shirt)

        except ServiceResourceDoesNotExistException:
            return Response(
                {"message": "Resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(serializer.data, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = ShirtSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            shirt = self.service.update(id=int(pk), **request.data)
        except ServiceResourceDoesNotExistException:
            return Response(
                {"message": "Resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ShirtSerializer(shirt)
        return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            self.service.delete(pk)
        except ServiceResourceDoesNotExistException:
            return Response(
                {"message": "Resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response("", status.HTTP_200_OK)
