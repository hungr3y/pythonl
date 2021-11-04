class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def my_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str) and new_email.count('@')==1 \
            and '.' in new_email[new_email.find('@'):]:
            self.__email = new_email
        else:
            print('Ошибочная почта')

    def delete_email(self):
        del self.__email

    my_email = property(my_email)
    # my_email = my_email.setter(set_email)
    # my_email = my_email.deleter(delete_email)


# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # Ошибочная почта
# k.email = 'prince@still@.wait'  # Ошибочная почта
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait
