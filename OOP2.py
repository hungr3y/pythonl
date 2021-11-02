class Laptop:
    def __init__(self, brand, model, price):
        self.model = model
        self.brand = brand
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'




laptop1=Laptop('Asus', '18-bdfx', 37000)
laptop2=Laptop('Samsung', '13-bsdf0xx', 47000)


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"

