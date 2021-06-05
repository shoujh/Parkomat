import unittest
from ParkingMeter import *


class TestParkMeter(unittest.TestCase):
    def setUp(self):
        self.p = ParkingMeter()


class TestInit(TestParkMeter):  # tworzenie obiektu ParkMeter i sprawdzanie działania funkcji __init__
    def testInitialPlate(self):
        self.assertEqual(self.p.getPlate(), '')

    def testInitialMoneyList(self):
        self.assertEqual(self.p.getMoney(), [])

    def testInitialTotalsum(self):
        self.assertEqual(self.p.getTotalsum(), 0)

    def testInitialLeaveTime(self):
        self.assertEqual(self.p.getTime(), self.p.getLeaveTime())


class TestHour(TestParkMeter):  # test 1. (niepoprawna godzina, godzina 12:34)
    def testSetWrongHour(self):
        temp = self.p.getTime()

        self.assertEqual(self.p.setTime('2021', '13', '21', 26, 30, 0), "Niepoprawna data lub godzina")  # komunikat
        self.assertEqual(temp, self.p.getTime())  # czas się nie zmienił

    def testSetTwelveThirtyFourHour(self):
        self.p.setTime('2020', '12', '21', 12, 34, 0)
        h = str(self.p.getTime())
        h = h.split(' ', 2)

        self.assertEqual(h[1], '12:34:00')  # sprawdzenie ustawienia godziny na 12:34


class TestInsertMoney(TestParkMeter):
    def testInsert2_4_5_5PLN(self):  # test 2.
        self.p.setTime('2021', '5', '24', 8, 0, 0)

        self.p.addCoin(2, 1)

        self.assertEqual(self.p.getTime() + timedelta(hours=1), self.p.getLeaveTime())
        # obecny czas + 1h = termin wyjazdu

        self.p.addCoin(2, 2)

        self.assertEqual(self.p.getTime() + timedelta(hours=2), self.p.getLeaveTime())
        # obecny czas + 2h = termin wyjazdu

        self.p.addCoin(5, 1)

        self.assertEqual(self.p.getTime() + timedelta(hours=3), self.p.getLeaveTime())
        # obecny czas + 3h = termin wyjazdu

        self.p.addCoin(5, 1)

        self.assertEqual(self.p.getTime() + timedelta(hours=4), self.p.getLeaveTime())
        # obecny czas + 4h = termin wyjazdu

    def testInsertUntilNextDay(self):  # test 3.
        self.p.setTime('2021', '5', '24', 17, 30, 0)
        self.p.addCoin(2, 3)
        self.p.addCoin(5, 1)

        self.assertEqual(self.p.getTime() + timedelta(hours=15), self.p.getLeaveTime())
        # 12h ponieważ parkomat nieczynny od 20 do 8 oraz 3h za wrzucenie 11 zł

    def testInsertUntilNextWeek(self):  # test 4.
        self.p.setTime('2021', '5', '21', 17, 30, 0)
        self.p.addCoin(2, 3)
        self.p.addCoin(5, 1)

        self.assertEqual(self.p.getTime() + timedelta(hours=63), self.p.getLeaveTime())
        # 12h ponieważ parkomat nieczynny od 20 do 8 oraz 3h za wrzucenie 11 zł oraz 48h za pominięcie weekendu

    def testInsert1PLN(self):  # test 5.
        self.p.setTime('2021', '5', '21', 17, 30, 0)
        self.p.addCoin(1, 1)

        self.assertEqual(self.p.getTime() + timedelta(minutes=30), self.p.getLeaveTime())
        # 1zł = połowa pierwszej godziny

    def testInsert200GR(self):  # test 6.
        self.p.setTime('2021', '5', '21', 13, 30, 0)
        self.p.addCoin(0.01, 200)

        self.assertEqual(self.p.getTime() + timedelta(hours=1), self.p.getLeaveTime())
        # 2zł = pierwsza godzina

    def testInsert201GR(self):  # test 7.
        self.p.setTime('2021', '5', '21', 13, 45, 0)

        self.assertEqual(self.p.addCoin(0.01, 201), "Proszę o wrzucenie innego nominału")  # komunikat
        self.assertEqual(self.p.getLeaveTime(), self.p.getTime())  # obecny czas i termin wyjazdu są sobie równe


class TestConfirmPress(TestParkMeter):
    def testConfirmWithoutMoneyInserted(self):  # test 8.
        self.assertEqual(self.p.confirmPress('KLI993X'), "Nie wrzucono żadnych monet")  # komunikat

    def testConfirmWithoutRegistrationPlate(self):  # test 9.
        self.p.addCoin(0.01, 1)

        self.assertEqual(self.p.confirmPress(''), "Niepoprawna rejestracja")  # komunikat

    def testConfirmWithoutMoneyAndRegistration(self):  # połączenie testu 8. i 9.
        self.assertEqual(self.p.confirmPress(''),
                         "Niepoprawna rejestracja oraz nie wrzucono żadnych monet")  # komunikat


if __name__ == '__main__':
    unittest.main()
