"""
1) Создайте дескриптор, который будет делать поля класса управляемые им
доступными только для чтения.
"""


class UserCountryDescriptor:
    def __init__(self, country: str):
        self.country = country

    def __get__(self, instance, owner) -> str:
        return self.country

    def __set__(self, instance, value):
        raise AttributeError("This field is read-only | scenario 1 __set__")  # scenario 1
        # pass  # scenario 2

    def __delete__(self, instance):
        raise AttributeError("This field is read-only | scenario 1 __delete__")  # scenario 1
        # pass  # scenario 2


class User:
    country = UserCountryDescriptor('Ukraine')

    def __init__(self, name: str, surname: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(surname, str):
            raise TypeError("Surname must be a string")

        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}, {self.country}'


user_1 = User('John', 'Smith')
print(user_1)

tmp = user_1.country
print(tmp)

# user_1.country = 'Germany'  # AttributeError: This field is read-only | scenario 1 __set__
# print(user_1)

# del user_1.country  # AttributeError: This field is read-only | scenario 1 __delete__
