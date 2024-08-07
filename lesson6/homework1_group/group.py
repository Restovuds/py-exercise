import settings
from student import Student
from my_exceptions.student_in_group import StudentInGroupException
from group_iter import GroupIter


class Group:
    """
    defines group of students
    """

    def __init__(self, name: str):
        """
        :param name: name of the group
        """
        if not isinstance(name, str):
            raise TypeError('Group name must be a string')

        self.name = name
        self.students = []

    def add_student(self, student: Student):
        """
        :param student: obj of Student
        :return: -
        """
        if not isinstance(student, Student):
            raise TypeError('Student must be an instance of Student')

        if len(self.students) >= settings.MAX_STUDENTS:
            raise StudentInGroupException(settings.MAX_STUDENTS, "Maximum number of students allowed")

        if student in self.students:
            raise ValueError('Student already in group')

        self.students.append(student)

    def remove_student(self, student: Student):
        """
        :type student: object
        :param student: obj of Student
        :return: -
        """
        if not isinstance(student, Student):
            raise TypeError('Student must be an instance of Student')

        if student not in self.students:
            raise ValueError('Student not in group')

        self.students.remove(student)

    def search_student(self, surname: str) -> list:
        """
        :param surname: surname of student
        :return: list of students
        """
        if not isinstance(surname, str):
            raise TypeError('Surname must be a string')

        res = []
        for student in self.students:
            if student.surname.lower() == surname.lower():
                res.append(student)

        return res

    def __iter__(self):
        return GroupIter(self.students)

    def __str__(self) -> str:
        return f'Group: {self.name} \n Students list: \n ' + '\n'.join(map(str, self.students))
