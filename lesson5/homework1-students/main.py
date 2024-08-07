from group import Group
from student import Student
from my_exceptions.student_in_group import StudentInGroupException

if __name__ == '__main__':
    group = Group('410-i')

    students = []

    try:
        students = ["",
                    Student("", "Чеслава", '12-12-12'),
                    Student("Улицька", "Купава", '12-12-12'),
                    Student("Ерстенюк", "Евеліна", '12-12-12'),
                    Student("Забіла", "Радченко", '12-12-12'),
                    Student("Марковичі", "Радченко", '12-12-12'),
                    Student("Їжакевич", "Далемир", '12-12-12'),
                    Student("Лугова", "Єкатерина", '12-12-12'),
                    Student("Харченко", "Братко", '12-12-12'),
                    Student("Якобовський", "Ус", '12-12-12'),
                    Student("Єрченко", "Златодан", '12-12-12')]

    except (StudentInGroupException, TypeError, ValueError) as e:
        print(e)

    for student in students:
        try:
            group.add_student(student)
        except (StudentInGroupException, TypeError, ValueError) as e:
            print(e)

    print(group)
    print('\n')
    print("\n".join(map(str, group.search_student('Радченко'))))
