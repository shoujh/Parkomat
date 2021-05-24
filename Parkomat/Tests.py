import unittest
from ParkingMeter import *


class TestParkMeter(unittest.TestCase):
    def setUp(self):
        self.p = ParkingMeter()


class TestInit(TestParkMeter):  # tworzenie obiektu ParkMeter i sprawdzanie działania funkcji __init__
    def setUp(self):
        super().setUp()

    def testInitialPlate(self):
        self.assertEqual(self.p.getPlate(), '')

    def testInitialMoneyList(self):
        self.assertEqual(self.p.getMoney(), [])

    def testInitialTotalsum(self):
        self.assertEqual(self.p.getTotalsum(), 0)

    def testInitialLeaveTime(self):
        self.assertEqual(self.p.getTime(), self.p.getLeaveTime())


class TestHour(TestParkMeter):  # test 1. (niepoprawna godzina, godzina 12:34)
    def setUp(self):
        super().setUp()

    def testSetWrongHour(self):
        temp = self.p.getTime()
        self.assertTrue(self.p.setTime('2021', '13', '21', 26, 30, 0), "Niepoprawna data lub godzina")  # komunikat
        self.assertEqual(temp, self.p.getTime())

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
        self.assertEqual(self.p.getTime()+timedelta(hours=15), self.p.getLeaveTime())
        # 12h ponieważ parkomat nieczynny od 20 do 8 oraz 3h za wrzucenie 11 zł
if __name__ == '__main__':
    unittest.main()
