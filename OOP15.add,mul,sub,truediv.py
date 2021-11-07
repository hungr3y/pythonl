class Vector:

    def __init__(self, *args):
        self.values = []
        for n in args:
            if isinstance(n, int):
              self.values.append(n)

    def __str__(self):
        if len(self.values) == 0:
            return f"Пустой вектор"
        else:
            self.values.sort()
            return f'Вектор{tuple(self.values)}'

    def __add__(self, other):




v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
# v1+[1,2,3]

for i in v1.values:
    b=i+3
    print(i+3)
    v1.values.pop(i)

    print(v1.values)

# v2 = Vector(3,4,5)
# print(v2) # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3) # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4) # печатает "Вектор(9, 11, 13)"
# v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
# v5 + 'hi' # печатает "Вектор нельзя сложить с hi"