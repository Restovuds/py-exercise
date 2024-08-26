# solid

# Single responsibility # Принцип єдиної відповідальності
# Open-closed # Принцип відкритості-закритості
# Liskov substitution principle / LSP # Принцип підстановки Барбари Лисков


from abc import ABC, abstractmethod

class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i, price in enumerate(self.prices):
            total += self.quantities[i] * price
        return total





class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order: Order):
        print('Processing debit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order: Order):
        print('Processing credit payment type')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class PayPallPaymentProcessor(PaymentProcessor):
    def __init__(self, email: str):
        self.email = email

    def pay(self, order: Order):
        print('Processing payment type')
        print(f'Verifying email: {self.email}')
        order.status = 'paid'



order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())

processor = DebitPaymentProcessor('0372846')

processor.pay(order)









