from human import Human


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

        if not isinstance(date_of_birth, str):
            raise TypeError('date_of_birth must be of type str')

        try:
            super().__init__(name, surname)
        except TypeError as err:
            raise TypeError(err)

        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'\t{ super().__str__()} - {self.date_of_birth}'