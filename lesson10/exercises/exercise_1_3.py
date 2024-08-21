"""
Создайте класс LoggedProperty с дескриптором, который будет логировать доступ к атрибуту (как чтение, так и запись).
Логирование может быть реализовано через простой вывод в консоль.
"""

class LoggedProperty:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance_self, value):
        print(f'Setting {self.name} to {value}')
        instance_self.__dict__[self.name] = value

    def __get__(self, instance_self, instance_class):
        print(f'Getting {self.name}')
        return instance_self.__dict__[self.name]


class User:
    login = LoggedProperty('login')
    password = LoggedProperty('password')

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        return f'{self.login} {self.password}'


u1 = User('admin', '<PASSWORD>')
print(u1)
u2 = User('admin1', '<PASSWORD>1')
print(u2)