"""
Создайте класс LoggedProperty с дескриптором, который будет логировать доступ к атрибуту (как чтение, так и запись).
Логирование может быть реализовано через простой вывод в консоль.
"""

class LoggedProperty:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        print(f'Setting {self.name} to {value}')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print(f'Getting {self.name}')
        return instance.__dict__[self.name]


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