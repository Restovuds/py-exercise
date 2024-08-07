class Customer:
    def __init__(self, name, surname, phone):
        if not isinstance(name, str):
            raise TypeError("Name must be of type string")

        if not isinstance(surname, str):
            raise TypeError("Surname must be of type string")

        if not isinstance(phone, str):
            raise TypeError("Phone must be of type string")

        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self) -> str:
        return f'{self.surname} {self.name[0]}., {self.phone}'
