from customer import Customer
from product import Product


class Cart:
    def __init__(self, customer: Customer = None):
        if customer is not None:
            if not isinstance(customer, Customer):
                raise TypeError("Customer must be of type Customer")

        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float) -> None:
        if not isinstance(product, Product):
            raise TypeError("Product must be of type Product.")

        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity must be of type int or float.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total(self) -> int | float:
        res = 0
        for index, item in enumerate(self.products):
            res += item.price * self.quantities[index]
        return res

    def __len__(self):
        return len(self.products)

    def __getitem__(self, index) -> Product:
        if isinstance(index, (slice, int)):
            return self.products[index]

    def __str__(self) -> str:
        res = f'{self.customer} \n'
        for index, item in enumerate(self.products):
            res += f' {item} x {self.quantities[index]} ({item.price * self.quantities[index]} UAH)\n'
        res += f'Total: {self.total()} UAH\n'
        return res
