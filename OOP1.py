class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, coord2):
        if hasattr(coord2, 'x'):
            return(((coord2.x-self.x)**2+(coord2.y-self.y)**2)**0.5)

        else:
            print('Передана не точка')


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
print(d)
p1.get_distance(10) # Распечатает "Передана не точка"