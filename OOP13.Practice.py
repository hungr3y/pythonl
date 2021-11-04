from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'abracadabra'

    @property
    def secret(self):
        s = input('Введите ваш пароль')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Доступ закрыт')

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_password_in_list(password):
        with open('password_list.txt', 'r') as f:
            for line in f:
                if line.strip() == password:
                    return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Parol doljen bit STR')
        if len(value) < 4:
            raise ValueError('Parol doljen bit bolshe 4')
        if len(value) > 12:
            raise ValueError('Parol doljen bit menshe 12')
        if not User.is_include_number(value):
            raise ValueError('Parol doljen soderjat cifru')
        if User.is_password_in_list(value):
            raise ValueError('Pridumai parol pooriginalnei')
        self.__password = value


k = User('asd', '123456')
