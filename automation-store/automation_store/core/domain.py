# shoes, pants, shirts


from decimal import Decimal


class Shirt:
    def __init__(
        self,
        size: None,
        color: None,
        brand: None,
        price: Decimal = 0.0,
        id: int = None,
    ) -> None:
        self.id = id
        self.size = size
        self.color = color
        self.brand = brand
        self.price = price

    @property
    def slug(self):
        return self.brand + self.size

    def update(self, **data):
        for key, value in data.items():
            setattr(self, key, value)


class ShirtService:
    list_of_shirt = [
        Shirt(1, "M", "Black", "Nike", 100),
        Shirt(2, "GG", "Pink", "Nike", 120),
    ]

    def get(self, pk):
        ...

    def create(self, item: Shirt):
        ...

    def delete(self, pk):
        ...

    def update(self, item: Shirt):
        ...

    def __contains__(self, item: Shirt):
        ...