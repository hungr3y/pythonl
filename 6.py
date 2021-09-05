n = int(input())
popart = {}
popart2 = []
def f(a):
   return(a)*2
for i in range(n):
    x = int(input())
    if x in popart:
        popart2.append(popart[x])
    else:
        popart[x] = f(x)
        popart2.append(f(x))
for j in popart2:
    print(j)


