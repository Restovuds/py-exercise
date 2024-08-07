class Product:
    def __init__(self, title: str, price: int | float):
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be of type int or float")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        self.title = title
        self.price = price

    def __str__(self) -> str:
        return f'{self.title} : {self.price} UAH'
