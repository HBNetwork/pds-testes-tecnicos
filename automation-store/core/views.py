from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TShirtSerializer
from rest_framework import status

# Create your views here.
class TshirtViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def create(self, request):
        serializer = TShirtSerializer(data=request.data)
        if serializer.is_valid():
            return Response([], status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
