import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('мой номер - 444-444-5432. а еще есть 222-543-6787')
print('Найденный телефонный номер: ' + mo.group())


wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('123456s7890'))

a = ['asd',  'gqwg', 'ghswdg']
b = ['asd1', 'gqwg1', 'ghswdg1']
for i in a:
    print(i.rjust(6))



