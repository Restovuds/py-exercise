import re


def get_all_urls(text: str) -> list:
    """
    Вилучення URL-адрес: Створіть регулярний вираз, який вилучає всі URL-адреси з тексту.
    """

    matches = re.findall(r'(https?://\S+)', text)

    return matches


string = """A regular expression is a sequence of characters that specifies a search pattern in text. Usually such 
patterns are used by string-searching algorithms for “find” or “find and replace” operations on strings, or for 
input validation.
https://www.tutorialspoint.com/python/python_reg_expressions.html
Visit the following resources to learn more:
http://docs.python.org/3/library/re.html
articlePython Regular Expressions
articlePython - Regular Expressions
"""

print(get_all_urls(string))