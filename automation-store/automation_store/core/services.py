from decimal import Decimal

from .domain import Shirt
from .exceptions import ServiceResourceNotFoundException


class ShirtService:
    def __init__(self) -> None:
        self.list_of_shirt = [
            Shirt("M", "Black", "Nike", Decimal(100), 1),
            Shirt("GG", "Pink", "Nike", Decimal(120), 2),
        ]
    
    def list(self):
        return self.list_of_shirt

    def get(self, pk):
        shirt = list(filter(lambda shirt: shirt.id == int(pk), self.list_of_shirt))

        if not shirt:
            raise ServiceResourceNotFoundException("Shirt")

        return shirt[0]

    def create(self, item: Shirt):
        item.id=len(self.list_of_shirt)
        self.list_of_shirt.append(item)

        return item

    def delete(self, pk):
        shirt = self.get(pk)

        self.list_of_shirt.remove(shirt)

    def update(self, id, data: dict):
        shirt = self.get(id)
        
        shirt.size = data.get("size", shirt.size)
        shirt.color = data.get("color", shirt.color)
        shirt.brand = data.get("brand", shirt.brand)
        shirt.price = data.get("price", shirt.price)

        return shirt

    def __contains__(self, item: Shirt):
        ...
