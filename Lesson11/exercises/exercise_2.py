"""
Suppose we want to create a program that models different types of animals, such as dogs, cats, and birds.
We can create an abstract class called Animal that defines the common interface for all animals, and then create
derived classes for each specific animal:
"""

import abc


class DoSomethingExampleABC(abc.ABC):
    @abc.abstractmethod
    def do_something(self, value):
        pass


class DoMul42(DoSomethingExampleABC):
    def __init__(self):
        self.value = None

    def do_something(self, value):
        self.value = value * 42
        return self.value


test = DoMul42()
print(test.do_something(10))



