"""
Создайте класс Temperature, который использует дескриптор для управления доступом к атрибуту температуры. Этот класс должен иметь следующие особенности:

1 Атрибут celsius должен хранить температуру в градусах Цельсия.
2 Когда температура устанавливается, она должна автоматически конвертироваться в Кельвины и Фаренгейты и сохраняться в соответствующих атрибутах.
3 Реализуйте методы для получения температуры в Кельвинах и Фаренгейтах.
"""



class Temperature:
    class Celsius:
        def __get__(self, instance, owner):
            return instance.__dict__['_celsius']

        def __set__(self, instance_self, value):
            instance_self.__dict__['_celsius'] = value
            instance_self.__dict__['_kelvin'] = value + 273.15
            instance_self.__dict__['_fahrenheit'] = value * 9 / 5 + 32

    class Fahrenheit:
        def __get__(self, instance_self, instance_class):
            return instance_self.__dict__['_fahrenheit']

    class Kelvin:
        def __get__(self, instance_self, instance_class):
            return instance_self.__dict__['_kelvin']

    celsius = Celsius()
    fahrenheit = Fahrenheit()
    kelvin = Kelvin()

    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f'{self.celsius} == {self.fahrenheit} == {self.kelvin}'


temperature = Temperature(30)
print(temperature)

