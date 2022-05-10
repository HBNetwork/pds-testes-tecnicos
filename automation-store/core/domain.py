# shoes, pants, shirts


class Shirt:
    def __init__(
        self,
        id: None,
        size: None,
        color: None,
        brand: None,
        price: None,
    ) -> None:
        self.id = id
        self.size = size
        self.color = color
        self.brand = brand
        self.price = price

    @property
    def slug(self):
        return self.brand + self.size
