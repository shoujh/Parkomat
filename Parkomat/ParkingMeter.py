from datetime import datetime, timedelta
from Coin import *

letters_numbers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


class ParkingMeter:  # klasa Parkomat
    # przechowuje listę monet, tablice rejestracyjną, aktualny czas, termin wyjazdu oraz sumę wrzuconych monet
    def __init__(self):
        self._money = []
        self._plate = ''
        self._time = datetime.now()
        self._leave = self._time
        self._totalsum = 0

    def __str__(self):
        return 'BILET: rejestracja: {}, czas zakupu: {}, termin wyjazdu: {}'.format(self._plate, self._time,
                                                                                    self._leave)

    def getAmountOfCoin(self, coin):  # ilość monet danego nominału w parkomacie
        coin = Coin(coin)
        count = 0
        for i in range(len(self._money)):
            if coin.getValue() == self._money[i].getValue():
                count += 1
        return count

    def getPlate(self):  # zwraca tablice
        return self._plate

    def getMoney(self):  # zwraca listę monet
        return self._money

    def getTotalsum(self):  # zwraca sumę wrzuconych monet
        return self._totalsum

    def getLeaveTime(self):  # zwraca termin wyjazdu
        return self._leave

    def getTime(self):  # zwraca aktualny czas
        return self._time

    def zeroSumandLeave(self): # zeruje sumę oraz resetuje termin wyjazdu
        self._totalsum = 0
        self._leave = self._time

    def setTime(self, year, month, day, hour, minute, second):  # zmiana aktualnego czasu
        try:
            dt = datetime.strptime(str(day + ' ' + month + ' ' + year), '%d %m %Y')
            d = dt.replace(hour=hour, minute=minute, second=second)
        except:
            return 'Niepoprawna data lub godzina'
        self._time = d
        self._leave = self._time
        self._totalsum = 0

    def checkPlate(self, plate) -> bool:  # sprawdzenie poprawności rejestracji
        if plate == '' or plate == '\n':
            return False
        plate = plate.upper()
        plate = plate.strip()
        for i in range(len(plate)):
            if plate[i] not in letters_numbers:
                return False
        else:
            self._plate = plate
            return True

    def checkCoin(self, coin, amount) -> bool:  # bool czy przy wrzucaniu danych monet zostanie przekroczony limit
        if coin in coins:
            count = self.getAmountOfCoin(coin)
            if amount + count > 200:
                return False
        return True

    def nextDay(self, amount):  # przejście na x kolejnych dni i ustawienie czasu na 8:00
        self._leave += timedelta(days=amount)
        self._leave = self._leave.replace(hour=8, minute=0, second=0, microsecond=0)

    def addGr(self, delta):  # doliczenie wartości pojedynczego grosza oraz czasu odpowiadającemu groszowi
        if self._totalsum == 0:
            if int(self._leave.hour) < 8:
                self.nextDay(1)
            if int(self._leave.hour) >= 20:
                self.nextDay(1)
            if self._leave.isoweekday() == 6:
                self.nextDay(2)
            if self._leave.isoweekday() == 7:
                self.nextDay(1)
        secaftertwenty = 0
        self._totalsum += Decimal(0.01)
        self._leave += timedelta(seconds=delta)
        if int(self._leave.hour) >= 20 or int(self._leave.hour) < 8:
            if self._totalsum != 0:
                secaftertwenty = str(self._leave).split(' ', 1)
                secaftertwenty = secaftertwenty[1].split(':', 2)
                secaftertwenty = float(secaftertwenty[2])
            if 20 <= int(self._leave.hour) <= 23:
                self.nextDay(1)
            else:
                self.nextDay(0)
        if self._leave.isoweekday() == 6:
            self.nextDay(2)
        if self._leave.isoweekday() == 7:
            self.nextDay(1)
        self._leave += timedelta(seconds=secaftertwenty)

    def addCoin(self, coin, amount):  # wrzucenie monet danego typu w podanej ilości
        if self.checkCoin(coin, amount):
            coin = Coin(coin)
            gr = coin.getValue() * 100
            for i in range(amount):
                self._money.append(coin)
                for c in range(int(gr)):
                    if self._totalsum < 2.0:
                        self.addGr(18)
                    elif self._totalsum < 6.0:
                        self.addGr(9)
                    else:
                        self.addGr(7.2)
            return "Zaktualizowano czas wyjazdu: {}".format(self._leave)
        else:
            return "Proszę o wrzucenie innego nominału"

    def confirmPress(self, plate):  # zatwierdzenie wydania biletu z parkomatu
        x = False
        y = False
        if not self.checkPlate(plate):
            y = True
        if self.getTime() == self.getLeaveTime():
            x = True
        if x is False and y is False:
            temp = str(self)
            self.zeroSumandLeave()
            return temp
        elif x is True and y is True:
            return "Niepoprawna rejestracja oraz nie wrzucono żadnych monet"
        elif x is True:
            return "Nie wrzucono żadnych monet"
        elif y is True:
            return "Niepoprawna rejestracja"
