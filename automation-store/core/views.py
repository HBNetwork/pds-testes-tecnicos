from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ShirtSerializer
from rest_framework import status
from .domain import Shirt

# Create your views here.
class ShirtViewSet(viewsets.ViewSet):
    list_of_shirt = [
        Shirt(1, "M", "Black", "Nike", 100),
    ]

    def create(self, request):
        serializer = ShirtSerializer(data=request.data)
        if serializer.is_valid():
            return Response([], status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = ShirtSerializer(self.list_of_shirt, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # filter X list comprehension
        shirt = list(filter(lambda shirt: shirt.id == int(pk), self.list_of_shirt))
        # shirt = [s for s in self.list_of_shirt if s.id == int(pk)][0]

        if not shirt:
            return Response(
                {"message": "Resource not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ShirtSerializer(shirt[0])
        return Response(serializer.data, status.HTTP_200_OK)
