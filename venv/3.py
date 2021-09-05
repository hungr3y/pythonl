stroka = input()
strokal = stroka.lower()
g = 'G'
c = 'C'
e = ''
bg = s.upper().count(g)
bc = s.upper().count(c)
b_long = (s.upper().count(e)-1)
print(((bc+bg)/b_long)*100)

*******************

a = input()
i = 0
j = 1
l = len(a)
n = 1
while i != l - 1:
    if a[i] == a[j]:
        i += 1
        j += 1
        n += 1
    elif a[i] != a[j]:
        print(a[i], n, sep='', end='')
        i += 1
        j += 1
        n = 1
print(a[i], n, sep='', end='')

stroka = input()
new = 0
strokal = stroka.lower()
print(new.count(strokal))