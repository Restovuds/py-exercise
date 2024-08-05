import settings


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
    """
    defines person
    """

    def __init__(self, name: str, surname: str):
        """
        :param name: name op person
        :param surname: surname of person
        """
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.surname} {self.name}'


# task 2
class Student(Human):
    """
    defines student
    """

    def __init__(self, name: str, surname: str, date_of_birth: str):
        """
        :param name: name op person
        :param surname: surname of person
        :param date_of_birth: date of birth of person
        """
        super().__init__(name, surname)
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'\t{ super().__str__()} - {self.date_of_birth}'


# task 3
COUNT_OF_STUDENTS = 10


class Group():
    """
    defines group of students
    """

    def __init__(self, name: str):
        """

        :param name: name of the group
        """
        self.name = name
        self.students = []

    def add_student(self, student: Student) -> int:
        """

        :param student: obj of Student
        :return: -1 when students more than allowed
                1 when student was added
                -2 when student already is in this group
        """
        if len(self.students) >= settings.MAX_STUDENTS:
            return -1

        if student not in self.students:
            self.students.append(student)
            return 1

        return -2

    def remove_student(self, student: Student) -> int:
        """
        :param student: obj of Student
        :return: 1 when student was removed
                -1 when student not found in this group
        """
        if student in self.students:
            self.students.remove(student)
            return 1

        return -1

    def search_student(self, surname: str) -> list:
        """
        :param surname: surname of student
        :return: list of students
        """
        res = []
        for student in self.students:
            if student.surname.lower() == surname.lower():
                res.append(student)

        return res

    def __str__(self):
        res = f'Group: {self.name} \n Students list: \n ' + '\n'.join(map(str, self.students))
        return res


if __name__ == '__main__':
    group = Group('410-i')

    students = []
    students.append(Student("Антків", "Твердогоста", '12-12-12'))
    students.append(Student("Трощинська", "Чеслава", '12-12-12'))
    students.append(Student("Улицька", "Купава", '12-12-12'))
    students.append(Student("Ерстенюк", "Евеліна", '12-12-12'))
    students.append(Student("Забіла", "Радченко", '12-12-12'))
    students.append(Student("Марковичі", "Радченко", '12-12-12'))
    students.append(Student("Їжакевич", "Далемир", '12-12-12'))
    students.append(Student("Лугова", "Єкатерина", '12-12-12'))
    students.append(Student("Харченко", "Братко", '12-12-12'))
    students.append(Student("Якобовський", "Ус", '12-12-12'))
    students.append(Student("Єрченко", "Златодан", '12-12-12'))

    for student in students:
        group.add_student(student)

    print(group)
    #group.remove_student(students[-2])
    #print(group)
    #print("".join(map(str, group.search_student('Радченко'))))
