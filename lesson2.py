# lesson code #

class ABase:
    def __init__(self):
        self.a = 10
        self.b = 20

    def method_1(self):
        return f'{self.a + self.b}'


class BChild(ABase):
    def __init__(self):
        super().__init__()
        self.c = 3

    def method_2(self):
        return "Hello moon"

    def method_1(self):
        super().method_1()
        return int(super().method_1()) - self.c


# x = BChild()
# print(x.method_1())
# print(x.method_2())

########################################################################################################################
class A:
    def method_1(self):
        return 'Hello from A'


class B:
    def method_1(self):
        return 'Hello from B'


class D(A, B):
    pass

# x = D()
# print(x.method_1())  # Hello from A

# print(D.__mro__)
# #  (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# HOMEWORK #############################################################################################################
