def string_to_file(f):
    def inner(*args, **kwargs):
        with open(f'{args[0].__class__.__name__}.txt', 'a') as file:
            string = f(*args, **kwargs)
            file.writelines(string)

        return f(*args, **kwargs)
    return inner


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @string_to_file
    def __str__(self):
        return f'{self.surname}\t{self.name[0]}.\t{self.age} years old\n'


humans = [
    Human('Oleh', 'Radchenko', '24'),
    Human('Dima', 'Rayko', '23'),
    Human('Vlad', 'Grishenko', '23'),
]

for human in humans:
    print(human, end='')
