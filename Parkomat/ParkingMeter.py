from datetime import datetime, timedelta
from Coin import *

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


class ParkingMeter:
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

    def getLeaveTime(self):
        return self._leave

    def getTime(self):
        return self._time

    def setTime(self, year, month, day, hour, minute, second):
        try:
            dt = datetime.strptime(str(day + ' ' + month + ' ' + year), '%d %m %Y')
            self._time = dt.replace(hour=hour, minute=minute, second=second)
        except:
            print('Niepoprawna data lub godzina')
        self._leave = self._time

    def checkPlate(self, plate):
        if plate != self._plate:
            self._totalsum = 0
            self._plate = plate
            self._leave = self._time

    def checkCoin(self, coin, amount):
        if coin in coins:
            count = self.getAmountOfCoin(coin)
            if amount + count > 200:
                return -1
        return 1

    def nextDay(self, amount):
        self._leave += timedelta(days=amount)
        self._leave = self._leave.replace(hour=8, minute=0, second=0, microsecond=0)

    def addGr(self, delta):
        self._totalsum += Decimal(0.01)
        self._leave += timedelta(seconds=delta)

    def timeEval(self):
        if self._leave.isoweekday() == 6:
            self.nextDay(2)
        if self._leave.isoweekday() == 7:
            self.nextDay(1)
        if int(self._leave.hour) >= 20 or int(self._leave.hour) < 8:
            self.nextDay(1)

    def addCoin(self, coin, amount, plate):
        self.checkPlate(plate)
        t = self.checkCoin(coin, amount)
        if t == 1:
            coin = Coin(coin)
            gr = coin.getValue() * 100
            for i in range(amount):
                self._money.append(coin)
                for c in range(int(gr)):
                    if self._totalsum < 2.0:
                        self.timeEval()
                        self.addGr(18)
                    elif self._totalsum < 6.0:
                        self.timeEval()
                        self.addGr(9)
                    else:
                        self.timeEval()
                        self.addGr(7.2)
        else:
            print("Proszę o wrzucenie innego nominału.")
        return self._leave

    def getTicket(self):
        return self._plate, self._time, self._leave
