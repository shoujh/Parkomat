from decimal import *
from ErrorHandler import WrongNominalException

coins = {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5}
banknotes = {10, 20, 50}



class Coin:
    def __init__(self, value):
        self._values = coins.union(banknotes)
        if value in self._values:
            self._value = Decimal(str(value))
        else:
            raise WrongNominalException("Nieznana moneta lub banknot")
        self._currency = 'zł'

    def __str__(self):
        return 'obiekt Coin, i = {}, k = {}'.format(self._value, self._currency)

    def __repr__(self):
        return 'Coin({},{})'.format(self._value, self._currency)

    def getValue(self):
        return self._value

    def getCurrency(self):
        return self._currency