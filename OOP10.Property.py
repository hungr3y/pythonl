class Money:

    def __init__(self, dollars, cents):
        self.total_cents = dollars,cents

    @property
    def my_dollars(self):
        return self.total_cents()
















k = Money(3, 50)
k.my_dollars
# k.total_cents()
