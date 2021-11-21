class Vector:

    def __init__(self, *args):
        self.values = [*args]
        for arg in self.values:
            if isinstance(arg, int):
                continue
            else:
                self.values.remove(arg)
        self.values = sorted(self.values)

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{self.values}'
        else:
            return f"Пустой вектор"

    def __add__(self, other):



v1 = Vector(1,4, 'asd',3,7)
print(v1) # печатает "Вектор(1, 2, 3)"