class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self) -> str:
        return f'{self.title} : {self.price} UAH'


class Customer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self) -> str:
        return f'{self.surname} {self.name[0]}., {self.phone}'


class Cart:
    def __init__(self, customer: Customer = None):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float) -> None:
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

    def __str__(self) -> str:
        res = f'{self.customer} \n'
        for index, item in enumerate(self.products):
            res += f' {item} x {self.quantities[index]} ({item.price * self.quantities[index]} UAH)\n'
        res += f'Total: {self.total()} UAH\n'
        return res


pr_1 = Product('Prod 1', 23)
pr_2 = Product('Prod 2', 123)
pr_3 = Product('Prod 3', 1543.3)

customer1 = Customer('Oleh', '<NAME>', 348973459708)
customer2 = Customer('<NAME>', 'Katya', 239082394803)

card_1 = Cart(customer1)
card_2 = Cart(customer2)

card_1.add_product(pr_1, 2)
card_1.add_product(pr_2, 0.3)

card_2.add_product(pr_1, 1)
card_2.add_product(pr_2, 1)
card_2.add_product(pr_3, 1)

print(card_1)
print(card_2)
