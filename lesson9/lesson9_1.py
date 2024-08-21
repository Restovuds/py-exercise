# def add_field(cls):
#     def inner(*args, **kwargs):
#         new_instance = cls(*args, **kwargs)
#         new_instance.count = 1
#         return new_instance
#     return inner
#
#
# @add_field
# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = "+str(self.x)+", y = "+str(self.y)+", z = "+str(self.z)+" ]"
#
#
# b = Box(1, 2, 3)
# print(b)
# print(type(b))
# print(b.count)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# class DecoratorClass:
#     def __init__(self, cls):
#         self.cls = cls
#         self.count = 0
#
#     def __call__(self, *arg, **name_args):
#         new_instance = self.cls(*arg, **name_args)
#         self.count += 1
#         return new_instance
#
#
# @DecoratorClass
# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = "+str(self.x)+", y = "+str(self.y)+", z = "+str(self.z)+" ]"
#
#
# box = Box(1, 2, 3)
# box2 = Box(2, 2, 2)
# print(Box.count)
# print(type(Box))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = " + str(self.x) + ", y = " + str(self.y) + ", z = " + str(self.z) + " ]"

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def up():
        print("up")

    @classmethod
    def print_class_info(cls):
        print(str(cls))


box_1 = Box(1, 2, 3)
box_1.print_class_info()
Box.print_class_info()

box_1.up()
Box.up()
