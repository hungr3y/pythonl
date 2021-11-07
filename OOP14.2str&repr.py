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

v1 = Vector(12,'hello', '5', 4, 3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"
