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
        self._start_hour = '8'
        self._end_hour = '20'

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
        self._leave = self._time

    def nextDay(self, amount):
        self._leave += timedelta(days=amount)
        self._leave = self._leave.replace(hour=8, minute=0)

    def hourVal(self, delta):
        if self._leave.isoweekday() == 6:
            self.nextDay(2)
        if self._leave.isoweekday() == 7:
            self.nextDay(1)
        if int(self._leave.hour) >= 20 or int(self._leave.hour) < 8:
            self.nextDay(1)
        self._totalsum += Decimal(0.01)
        self._leave += timedelta(seconds=delta)

    def addCoin(self, coin, amount, plate):
        if plate != self._plate:
            self._totalsum = 0
            self._plate = plate
            self._leave = self._time
        count = self.getAmountOfCoin(coin)
        if amount + count > 200:
            raise NotImplementedError
        coin = Coin(coin)
        gr = coin.getValue() * 100
        for i in range(amount):
            self._money.append(coin)
            for c in range(int(gr)):
                if self._totalsum < 2.0:
                    self.hourVal(18)
                elif self._totalsum < 6.0:
                    self.hourVal(9)
                else:
                    self.hourVal(7.2)
        return self._leave


s = Parkomat()
s.setTime('2021', '5', '21', 23, 45, 0)
print(s.getTime())
print(s.addCoin(2, 3, 'KR99632'))
print(s.addCoin(0.5, 5, 'KR99632'))
print(s.addCoin(0.01, 5, 'KR49652'))
print(s.getAmountOfCoin(2))
