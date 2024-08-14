#  lecture 10 code

# class A:
#     def __init__(self):
#         self.a = 10
#
#
# x = A()
# print(x.a)
# x.a = 20
# print(x.a)
#
# del x.a
# print(x.a)

#  properties # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  property( attrname, getter, setter, deleter ) == decorator

# class ExampleOne:
#     def __init__(self, price):
#         self.price = price
#
#     @property
#     def price(self):  # getter
#         return self.__price * 1.2  # price with tax
#
#     @price.setter
#     def price(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('Price must be an integer or float')
#         if value <= 0:
#             raise ValueError('Price must be greater than 0')
#
#         self.__price = value
#
#     @price.deleter
#     def price(self):
#         pass
#
#
# x = ExampleOne(2)
# print(x.price)
# x.price = 3.14
# print(x.price)
# del x.price
# print(x.price)


#  __getattr__ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         tmp = self.__dict__.items()
#         x = map(lambda item: f'{item[0]}: {str(item[1])}', tmp)
#         return '\n'.join(x)
#
#     #  Example 1
#     # def __getattr__(self, attr):
#     #     return 'Error'
#
#     def __getattr__(self, attr):
#         self.__dict__[attr] = None
#         return None
#
#
# cat_1 = Cat('Tom')
# print(cat_1)
#
# print(cat_1.example_1)  # Error
#
# print(cat_1.example_2)  # None
# print(cat_1.example_2)  # None
# print(cat_1)  # name: Tom  \n  example_1: None  \n  example_2: None


#  __getattribute__ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Cat:
#     allow_attribute_names = ('age', 'color', 'breed', 'weight')
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return '\n'.join(map(lambda item: f'{item[0]}: {str(item[1])}', self.__dict__.items()))
#
#     def __getattribute__(self, item):
#         try:
#             return object.__getattribute__(self, item)
#         except AttributeError:
#             if item in Cat.allow_attribute_names:
#                 self.__dict__[item] = None
#                 return None
#             else:
#                 return 'Error'
#
#
# cat_1 = Cat('Tima')
# print(cat_1.name)
# print(cat_1.age)
# print(cat_1.surname)


#  __setattr__, __delattr__  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Cat:
#     allow_attribute_names = ('age', 'color', 'breed', 'weight')
#
#     def __init__(self, name: str, age: int | float):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '\n'.join(map(lambda item: f'{item[0]}: {str(item[1])}', self.__dict__.items()))
#
#     def __setattr__(self, key, value):
#         if key == 'name' and not isinstance(value, str):
#             raise TypeError()
#         if key == 'age' and not isinstance(value, (int, float)):
#             raise TypeError()
#         if key == 'age' and value <= 0:
#             raise ValueError()
#
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         if item in self.__dict__:
#             del self.__dict__[item]
#
#         if item == 'name':
#             raise ValueError(f'Attribute "{item}" cannot be deleted')
#
#         raise ValueError(f'Attribute "{item}" cannot be deleted')
#
#
# # cat_1 = Cat('Tima', '2')  # TypeError
# cat_1 = Cat('Tima', 2)
# print(cat_1.name)
# print(cat_1.age)
#
# cat_1.age = 1  # ValueError
# cat_1.color = 'blue'
# del cat_1.dfgg  # Attribute "dfgg" cannot be deleted
#
# print(cat_1)


#  descriptors # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  need create class with:
#  1) __get__(self, instance_self, instance_class)
#  2) __set__(self, instance_self, value)
#  3) __delete__(self, instance_self)
#

# 1) __get__  # # # # # # # # # # # # # # # # # # # # # # # #
class MyDescriptor1:
    def __init__(self, n):
        self.n = n

    def __get__(self, instance_self, instance_class):
        print(self)
        print(instance_self)
        print(instance_class)
        return self.n * instance_self.p


class Box:
    def __init__(self, x, y, z):
        self.p = x * y * z

    volume = MyDescriptor1(2)


box1 = Box(1, 2, 3)


# 2) __set__  # # # # # # # # # # # # # # # # # # # # # # # #

class MyDescriptor2:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError()
        # raise AttributeError("Field is read-only")


class Sample:
    sample_field = MyDescriptor2('Hello')

    def __str__(self):
        return str(self.sample_field)


# a = Sample()
# print(a)
# print(a.sample_field)
# a.sample_field = 'World'
# print(a)


# 3) __delete__  # # # # # # # # # # # # # # # # # # # # # # # #

class MyDescriptor3:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        raise AttributeError("field is read-only")

    def __delete__(self, instance_self):
        raise AttributeError("cannot delete field")


class Sample1:
    sample_field = MyDescriptor3('Hello')

    def __str__(self):
        return str(self.sample_field)


a = Sample1()
print(a.sample_field)
# a.sample_field = 'World' # field is read-only
del a.sample_field  # AttributeError: cannot delete field
