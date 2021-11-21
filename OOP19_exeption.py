class Wallet:

    def __init__(self, currency, balance):
        self.currency = currency

        if not isinstance(self.currency, str):
            raise TypeError('Неверный тип валюты')

        if len(self.currency) > 3 or len(self.currency) < 3:
            raise NameError('Неверная длина названия валюты')

        if not self.currency.isupper():
            raise('Название должно состоять только из заглавных букв')

        self.balance = balance

    def __eq__(self, other):
        if not isinstance(self, Wallet) or not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')

        if self.currency == other.currency:
            if self.balance == other.balance:
                return True
            else:
                return False
        else:
            raise ValueError('Нельзя сравнить разные валюты')

    def __add__(self, other):








a = Wallet('ASD', 7)
b = Wallet('ASD', 6)
# class Gob:
#     currency = 7
# c = Gob()
# print(a == c)
print(a == b)



