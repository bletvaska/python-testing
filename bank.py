class BankAccount:
    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def credit(self, ammount):
        if type(ammount) != int:
            raise TypeError('Ammount is not an integer.')
        if ammount < 0:
            raise ValueError()
        self._balance += ammount

        if False:
            print('>> this is not covered')

    def withdraw(self, ammount):
        print(f'>> withdrawing {ammount}')
