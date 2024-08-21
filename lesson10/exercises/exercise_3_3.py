"""
Задача 3: Свойство с зависимостью от другого атрибута
Создайте класс Employee, который будет представлять сотрудника. У класса должен быть атрибут salary (зарплата),
и вычисляемое свойство bonus, которое будет возвращать 10% от зарплаты.

Требования:
Свойство salary должно быть доступным для чтения и записи.
Свойство bonus должно быть доступным только для чтения.
Если зарплата меньше 1000, бонус должен быть равен 0.
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def bonus(self):
        if self.salary < 1000:
            return 0

        return self.salary * 0.10

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError('Salary must be an positive integer or a float')

        self.__salary = value

    def __str__(self):
        return f'{self.name}, {self.salary} + bonus: {self.bonus}'


test_employee = Employee('John', 5000)
print(test_employee)
test_employee.salary = 100
print(test_employee)
test_employee.salary = 1000.10
print(test_employee)
test_employee.salary = 'a'
