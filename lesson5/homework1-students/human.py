class Human:
    """
    defines person
    """

    def __init__(self, name: str, surname: str):
        """
        :param name: name op person
        :param surname: surname of person
        """

        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(surname, str):
            raise TypeError('surname must be a string')

        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.surname} {self.name}'
