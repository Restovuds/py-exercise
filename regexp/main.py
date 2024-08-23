import re


# """
# re.search
# """
# string = '39801 356, 102 1111'
#
# pattern = r'\d{3} \d{2}'
# match = re.search(pattern, string)
# if match:
#     print(match.group()) #  801 35
# else:
#     print('No match')


# """
# re.findall
# """
# string = 'hello 12 hi 89. Howdy 34'
# pattern = r'\d+'
# print(re.findall(pattern, string)) #  ['12', '89', '34']


# """
# re.split
# """
# string = 'Twelve:12 Eighty nine:89.'
# pattern = r'\d+'
# print(re.split(pattern, string)) #  ['Twelve:', ' Eighty nine:', '.']


# """
# re.sub
# """
# string = 'abc 12' \
#     'de 23 \n f45 6'
# pattern = r'\s+'
# replace = ''
# print(re.sub(pattern, replace, string)) #  abc12de23f456


