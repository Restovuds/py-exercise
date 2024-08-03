class Buyer:
    """
    This class represents a buyer
    """

    def __init__(self, name, surname, address, phone, email):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.surname} \n{self.address} \n{self.phone} \n{self.email}'


buyer1 = Buyer("Oleh", "Radchenko", "My address", "0998877665", "test@test.test")
print(buyer1)

