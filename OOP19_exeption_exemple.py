class Wallet:

    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance

        if not isinstance(self.currency, str):
            raise TypeError('Неверный тип валюты')

        if len(self.currency) > 3 or len(self.currency) < 3:
            raise NameError('Неверная длина названия валюты')

        if not self.currency.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')

    def is_one_class_for_eq(self, other):
        if not isinstance(self, Wallet) or not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')

    def is_one_class_for_other(self, other):
        if not isinstance(self, Wallet) or not isinstance(other, Wallet):
            raise ValueError(f'Данная операция запрещена')

    def is_eq(self, other):
        if self.currency == other.currency:
            return True
        else:
            raise ValueError('Нельзя сравнить разные валюты')

    def __eq__(self, other):
        self.is_one_class_for_eq(other)
        self.is_eq(other)
        if self.balance == other.balance:
            return True
        else:
            return False

    def __add__(self, other):
        self.is_one_class_for_other(other)
        self.is_eq(other)
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        self.is_one_class_for_other(other)
        self.is_eq(other)
        return Wallet(self.currency, self.balance - other.balance)



