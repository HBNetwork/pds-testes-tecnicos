# shoes, pants, shirts


from decimal import Decimal


class Shirt:
    def __init__(
        self,
        size: None,
        color: None,
        brand: None,
        price: Decimal = Decimal(0),
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
