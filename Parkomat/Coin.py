from decimal import *

coins = {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5}  # lista nominałów monet
banknotes = {10, 20, 50}  # lista banknotów


class WrongNominalException(Exception):
    """
    Klasa wyjątku

    Wykorzystywana w przypadku próby utworzenia monety o niepoprawnym nominale.
    """
    def __init__(self, info):
        super().__init__(info)


class Coin:
    """
    Klasa przechowująca monetę/banknot
    """
    def __init__(self, value):
        """
        Konstruktor klasy Coin, przyjmuje nominał i tworzy obiekt o ile nominał jest poprawny (waluta zł)

        :param value: nominał
        """
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
        """
        Metoda zwracająca zmienną prywatną

        :return: nominał
        """
        return self._value

    def getCurrency(self):
        """
        Metoda zwracająca zmienną prywatną

        :return: waluta
        """
        return self._currency
