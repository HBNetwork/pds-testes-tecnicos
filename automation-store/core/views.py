from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ShirtSerializer
from rest_framework import status
from .domain import Shirt


# Create your views here.
class ShirtViewSet(viewsets.ViewSet):
    list_of_shirt = [
        Shirt(1, "M", "Black", "Nike", 100),
        Shirt(2, "GG", "Pink", "Nike", 120),
    ]

    def create(self, request):
        serializer = ShirtSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        self.list_of_shirt.append(
            Shirt(
                id=len(self.list_of_shirt),
                size=serializer["size"],
                color=serializer["color"],
                brand=serializer["brand"],
                price=serializer["price"],
            )
        )

        return Response([], status.HTTP_201_CREATED)

    def list(self, request):
        serializer = ShirtSerializer(self.list_of_shirt, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # filter X list comprehension
        shirt = list(filter(lambda shirt: shirt.id == int(pk), self.list_of_shirt))
        # shirt = [s for s in self.list_of_shirt if s.id == int(pk)][0]

        if not shirt:
            return Response(
                {"message": "Resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ShirtSerializer(shirt[0])
        return Response(serializer.data, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = ShirtSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        shirt = list(filter(lambda shirt: shirt.id == int(pk), self.list_of_shirt))

        if not shirt:
            return Response(
                {"message": "Resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = request.data

        shirt = shirt[0]

        if "size" in data:
            shirt.size = data["size"]
        if "color" in data:
            shirt.color = data["color"]
        if "brand" in data:
            shirt.brand = data["brand"]
        if "price" in data:
            shirt.price = data["price"]

        serializer = ShirtSerializer(shirt)
        return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        shirt = list(filter(lambda shirt: shirt.id == int(pk), self.list_of_shirt))

        if not shirt:
            return Response(
                {"message": "Resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        self.list_of_shirt.remove(shirt[0])

        return Response("", status.HTTP_200_OK)
