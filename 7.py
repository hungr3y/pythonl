n = input().split()
x = int(input())
t = True
for i in range(len(n)):
    result = int(n[i])
    n[i] = result
    if result == x:
        t = False
        print(i, end=' ')
if t:
    print('Отсутствует')
