"""
Создайте декоратор, который зарегистрирует декорируемый класс в
списке классов.
"""


class ClassDecorator:
    def __init__(self, cls):
        self.cls_list = []
        self.cls = cls

    def __call__(self, *args, **kwargs):
        new_instance = self.cls(*args, **kwargs)
        self.cls_list.append(new_instance)
        return new_instance

    def __str__(self):
        return f'{'\n'.join(map(str,self.cls_list))}'

@ClassDecorator
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Box ({self.x}, {self.y}, {self.z})'


box_1 = Box(1,2,3)
box_2 = Box(4,5,6)
box_3 = Box(7,8,9)

print(Box)


