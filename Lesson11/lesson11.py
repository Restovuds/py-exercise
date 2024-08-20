#  lecture 11

import abc


class A(abc.ABC):

    @abc.abstractmethod
    def method_1(self):
        pass

    def base_method(self):
        return 'some value'


# This is abstract class too:
# class A:
#     def method_1(self):
#         raise NotImplementedError  ## ##
#
#     def base_method(self):
#         return 'some value'

class ChildA1(A):
    def method_1(self):
        return 'Child A1'


# x = ChildA1()
# print(x.method_1())
# print(x.base_method())


#  Examples

class Animal:

    def say_hello(self):
        raise NotImplementedError


class Dog(Animal):
    def say_hello(self):
        return 'Woof'


class Cat(Animal):
    def say_hello(self):
        return 'Meow'


class Duck(Animal):
    def say_hello(self):
        return 'Qua'


def animal_farm(item):
    return item.say_hello()


obj_1 = Dog()
obj_2 = Cat()
obj_3 = Duck()

print(animal_farm(obj_1))
print(animal_farm(obj_2))
print(animal_farm(obj_3))
