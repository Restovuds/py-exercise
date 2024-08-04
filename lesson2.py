# lesson code #

class ABase:
    def __init__(self):
        self.a = 10
        self.b = 20

    def method_1(self):
        return f'{self.a + self.b}'


class BChild(ABase):
    def __init__(self):
        super().__init__()
        self.c = 3

    def method_2(self):
        return "Hello moon"

    def method_1(self):
        super().method_1()
        return int(super().method_1()) - self.c


# x = BChild()
# print(x.method_1())
# print(x.method_2())

########################################################################################################################
class A:
    def method_1(self):
        return 'Hello from A'


class B:
    def method_1(self):
        return 'Hello from B'


class D(A, B):
    pass


# x = D()
# print(x.method_1())  # Hello from A

# print(D.__mro__)
# #  (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# HOMEWORK #############################################################################################################
# task 1
class Human:
    def __init__(self, first_name, surname, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.second_name}\n'

# task 2
class Student(Human):
    def __init__(self, first_name, surname, second_name, receipt_date):
        super().__init__(first_name, surname, second_name)
        self.receipt_date = receipt_date

    def __str__(self):
        return f'{self.surname} {self.first_name[0]}. {self.second_name[0]}. \t{self.receipt_date}\n'

# task 3
class Group():
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if len(self.students) == 10:
            print(f'To much students in this group. Create the new one.')
            return False
        if student not in self.students:
            self.students.append(student)
        else:
            print(f'Student {student} already in this group.')

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print(f'Student {student} not in this group.')

    def search_student(self, surname):
        res = []
        for student in self.students:
            if student.surname.find(surname) > -1:
                res.append(student)

        return res

    def __str__(self):
        res = f'Group: {self.name}\n'
        res += f'Students list:\n'
        res += ''.join(map(str, self.students))
        return res

if __name__ == '__main__':
    group = Group('410-i')

    students = []
    students.append(Student("Антків", "Твердогоста" ,"Устимівна", ''))
    students.append(Student("Трощинська", "Чеслава" ,"Костянтинівна", ''))
    students.append(Student("Улицька", "Купава" ,"Левівна", ''))
    students.append(Student("Ерстенюк", "Евеліна" ,"Борисівна", ''))
    students.append(Student("Забіла", "Радченко" ,"Федорівна", ''))
    students.append(Student("Марковичі", "Радченко" ,"Соломонівна", ''))
    students.append(Student("Їжакевич", "Далемир" ,"Тарасович", ''))
    students.append(Student("Лугова", "Єкатерина" ,"Добромирівна", ''))
    students.append(Student("Харченко", "Братко" ,"Іванович", ''))
    students.append(Student("Якобовський", "Ус" ,"Світанович", ''))
    students.append(Student("Єрченко", "Златодан" ,"Світанович", ''))

    for student in students:
        group.add_student(student)

    print(group)

    group.remove_student(students[-2])

    print(group)

    print("".join(map(str,group.search_student('Радченко'))))