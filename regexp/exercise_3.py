import re

def replace_on_star(text: str) -> str:
    """
    Заміна всіх голосних букв на зірочку:
    Напишіть регулярний вираз, який замінює всі голосні букви в тексті на зірочку (*).
    """
    pattern = r'[AaEeYyUuIiOo]'
    return re.sub(pattern, '*', text)

string = 'Hello, my name is Oleh.'
print(replace_on_star(string))