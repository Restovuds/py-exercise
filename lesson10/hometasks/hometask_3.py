"""
3) Реализуйте свойство класса, которое обладает следующим
функционалом: при установки значения этого свойства в файл с заранее
определенным названием должно сохранятся время (когда устанавливали
значение свойства) и установленное значение.
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('log.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
ch.setFormatter(formatter)
logger.addHandler(ch)


class User:
    def __init__(self, name, login):
        self.name = name
        self.login = login
        self.password = '<PASSWORD>'

    def __str__(self):
        return f'[{self.login} | {self.password}] {self.name}'

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not isinstance(value, str):
            raise TypeError("Login should be a string")

        try:
            logger.info(f'Value of LOGIN=\'{self.login}\' changed to LOGIN=\'{value}\'')
        except AttributeError:
            pass

        self.__login = value




    @login.deleter
    def login(self):
        raise AttributeError("Can't delete attribute 'login'")


user_1 = User('John', 'john_login')
print(user_1.login)
user_1.login = 'john_login1'
user_1.login = 'john_login2'
