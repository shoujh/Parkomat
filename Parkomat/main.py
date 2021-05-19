from decimal import *
from datetime import datetime, timedelta


class WrongNominalException(Exception):
    def __init__(self, info):
        super().__init__(info)


class Coin:
    def __init__(self, value):
        self._values = {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50}
        if value in self._values:
            self._value = Decimal(str(value))
        else:
            raise WrongNominalException("Nieznana moneta lub banknot")
        self._currency = 'zł'

    def getValue(self):
        return self._value

    def getCurrency(self):
        return self._currency


class Parkomat:
    def __init__(self):
        self._money = []
        self._plate = ''
        self._time = datetime.now()
        self._leave = self._time
        self._totalsum = 0

    def getAmountOfCoin(self, coin):
        coin = Coin(coin)
        count = 0
        for i in range(len(self._money)):
            if coin.getValue() == self._money[i].getValue():
                count += 1
        return count

    def getTime(self):
        return self._time

    def setTime(self, year, month, day, hour, minute, second):
        dt = datetime.strptime(str(day + ' ' + month + ' ' + year), '%d %m %Y')
        self._time = dt.replace(hour=hour, minute=minute, second=second)

    def addCoin(self, coin, amount, plate):
        if plate != self._plate:
            self._totalsum = 0
            self._plate = plate
        count = self.getAmountOfCoin(coin)
        if amount + count > 200:
            raise NotImplementedError
        coin = Coin(coin)
        gr = coin.getValue() * 100
        for i in range(amount):
            self._money.append(coin)
            for c in range(int(gr)):
                if self._totalsum < 2.0:
                    self._totalsum += Decimal(0.01)
                    self._leave += timedelta(seconds=18)
                elif self._totalsum < 6.0:
                    self._totalsum += Decimal(0.01)
                    self._leave += timedelta(seconds=9)
                else:
                    self._totalsum += Decimal(0.01)
                    self._leave += timedelta(seconds=7.2)
        return self._leave


s = Parkomat()
print(s.getTime())
print(s.addCoin(2, 3, 'KR99632'))
print(s.addCoin(0.5, 5, 'KR99632'))

# print(s.getAmountOfCoin(0.1))
# s.setTime('2018', '5', '6', 12, 13, 45)
