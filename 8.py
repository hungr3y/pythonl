i = 0

def lol():
    global i
    if i > 10:
        return 0
    return 1
while lol():
    print('цикл идет')
    i += 1
print('Цикл закончился')