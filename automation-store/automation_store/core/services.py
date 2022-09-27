from decimal import Decimal

from automation_store.core.domain import Shirt
from automation_store.core.exceptions import ServiceResourceDoesNotExistException


class ShirtService:
    def __init__(self) -> None:
        self.list_of_shirt = [
            Shirt("M", "Black", "Nike", Decimal(100), 1),
            Shirt("GG", "Pink", "Nike", Decimal(120), 2),
        ]

    def list(self):
        return self.list_of_shirt

    def get(self, pk):
        if shirt := [
            shirt for shirt in self.list_of_shirt if int(shirt.id) == int(pk)
        ]:
            return shirt[0]
        else:
            raise ServiceResourceDoesNotExistException("Shirt")

    def create(self, item: Shirt):
        item.id = len(self.list_of_shirt) + 1
        self.list_of_shirt.append(item)

        return item

    def delete(self, pk):
        shirt = self.get(pk)

        self.list_of_shirt.remove(shirt)

    def update(self, **data):
        shirt = self.get(data.get("id"))

        for k, v in data.items():
            setattr(shirt, k, v)

        return shirt

    def __contains__(self, item: Shirt):
        ...
