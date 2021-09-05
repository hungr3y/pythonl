strokal = input().lower().split()
slovar = {}
for slova in strokal:
    if slova not in slovar:
        slovar[slova] = 1
    else:
        slovar[slova] += 1
for p in slovar:
    print(p, slovar[p], sep=" ");

