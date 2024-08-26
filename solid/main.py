# solid

# Single responsibility
# Open-closed


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
    def pay(self, order: Order, security_code: str):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print('Processing debit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order: Order, security_code: str):
        print('Processing credit payment type')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'




order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())

processor = DebitPaymentProcessor()
processor.pay(order, '0372846')









