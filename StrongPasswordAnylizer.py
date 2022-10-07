# Strong Password Analyser - программа определяющая сильный пароль или нет
# ильным паролем считается пароль, который
# 1) Содержит не меньше 8 символов
# 2) Содержит хотя-бы одну заглавную букву
# 3) Содержит хотя-бы одну строчную букву
# 4) Содержит хотя-бы одну цифру

'''
import re

password = 'As6'

bigMatch = re.search(r'[A-Z]', password)
samllMatch = re.search(r'[a-z]', password)
numMatch = re.search(r'[\d]', password)
if len(password) < 8:
    print('Cлишком короткий пароль')
if bigMatch == None:
    print('Нет заглавного символа')
if samllMatch == None:
    print('Нет строчного символа')
if numMatch == None:
    print('Нет цифры')
else:
    print('Cильный пароль')

    print(bigMatch)
    print(samllMatch)
    print(numMatch)

'''

import re

password = '123SaAss'

bigMatch = re.search(r'[A-Z]', password)
samllMatch = re.search(r'[a-z]', password)
numMatch = re.search(r'[\d]', password)
findSpace = re.search(r'\s', password)
if len(password) < 8 or bigMatch == None or samllMatch == None or numMatch == None:
    print('Слабый пароль')
elif findSpace != None:
    print('Пароль не должен содержать пробелов')
else:
    print('Сильный пароль')

    print('Длинна пароля составляет:', len(password), 'симвлов')
    print(bigMatch)
    print(samllMatch)
    print(numMatch)