# shoes, pants, shirts

class Shirts:
    def __init__(self) -> None:
        self.size
        self.color
        self.brand
        self.price

    @property
    def slug(self):
        return self.brand+self.size