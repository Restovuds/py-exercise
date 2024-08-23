import re



def number_regexp_check(number: str) -> bool:
    """
    Валідація номерів телефонів: Напишіть регулярний вираз, який валідує різні формати номерів телефонів
    (наприклад, +38(0XX)XXX-XX-XX) | (0XX)XXX-XX-XX.
    """
    pattern1 = r'\+38\(0\d{2}\)\d{3}\-\d{2}\-\d{2}'
    pattern2 = r'\(0\d{2}\)\d{3}\-\d{2}'
    if re.match(pattern1, number) or re.match(pattern2, number):
        return True
    return False

if __name__ == '__main__':
    number = input('Enter your phone number: "+38(0XX)XXX-XX-XX)": ')
    print(number, number_regexp_check(number), sep='\t')

