# solid

# Single responsibility # SRP # Принцип єдиної відповідальності
# Open-closed #	OCP # Принцип відкритості-закритості
# Liskov substitution principle # LSP # Принцип підстановки Барбари Лисков
# Interface segregation principle # ISP # Принцип розподілу інтерфейсу
# Dependency inversion principle # DIP # Принцип інверсії залежностей


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


class Authorizer(ABC):
    @abstractmethod
    def is_authorised(self) -> bool:
        pass


class AuthorizerSMS(Authorizer):
    def __init__(self):
        self.authorised = False

    def verify_code(self, code):
        print(f'Verifying code: {code}')
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


class AuthorizerGoogle(Authorizer):
    def __init__(self):
        self.authorised = False

    def verify_code(self, code):
        print(f'Verifying code: {code}')
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


class AuthorizerRobot(Authorizer):
    def __init__(self):
        self.authorised = False

    def not_a_robot(self, code):
        print(f'Verifying code: {code}')
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order: Order):
        if not self.authorizer.is_authorised():
            raise Exception('Not authorized')
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
    def __init__(self, email: str, authorizer: Authorizer):
        self.email = email
        self.authorizer = authorizer

    def pay(self, order: Order):
        if not self.authorizer.is_authorised():
            raise Exception('Not authorized')
        print('Processing PayPall payment type')
        print(f'Verifying email: {self.email}')
        order.status = 'paid'



order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('USB cable', 2, 5)

print(order.total_price())
authorizer = AuthorizerRobot()
authorizer.not_a_robot(123456)
processor = PayPallPaymentProcessor('test@test.com', authorizer)
processor.pay(order)









