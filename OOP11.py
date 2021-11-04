class Triangle:

    def __init__(self,first, second, third):
        self.first = first
        self.second = second
        self.third = third
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print("nachinayu kalkulirovat'")
            self.__area = self.first+self.second+self.third
        return self.first+self.second+self.third

b = Triangle(6,7,8)
b.area