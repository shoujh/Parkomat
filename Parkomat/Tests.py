import unittest
from ParkingMeter import *


class TestParkMeter(unittest.TestCase):
    """
    Klasa testowa

    Klasa, w której tworzymy obiekt ParkMeter, po tej klasie dziedziczą wszystkie klasy testowe
    """
    def setUp(self):
        self.p = ParkingMeter()


class TestInit(TestParkMeter):
    """
    Klasa testująca tworzenie obiektu Parkomat

    Sprawdza czy do przechowywanych zmiennych prywatnych zostały przypisane poprawne wartości
    """
    def testInitialPlate(self):
        self.assertEqual(self.p.getPlate(), '')

    def testInitialMoneyList(self):
        self.assertEqual(self.p.getMoney(), [])

    def testInitialTotalsum(self):
        self.assertEqual(self.p.getTotalsum(), 0)

    def testInitialLeaveTime(self):
        self.assertEqual(self.p.getTime(), self.p.getLeaveTime())


class TestHour(TestParkMeter):  # test 1.
    """
    Klasa testów zmiany czasu
    """
    def testSetWrongHour(self):
        """
        Test ustawienia niepoprawnej godziny, oczekiwany komunikat o błędzie oraz aktualny czas pozostaje niezmieniony
        """
        temp = self.p.getTime()

        self.assertEqual(self.p.setTime('2021', '13', '21', 26, 30, 0), "Niepoprawna data lub godzina")  # komunikat
        self.assertEqual(temp, self.p.getTime())  # czas się nie zmienił

    def testSetTwelveThirtyFourHour(self):
        """
        Test zmiany czasu na 12:34:00, oczekiwana godzina 12:34:00
        """
        self.p.setTime('2020', '12', '21', 12, 34, 0)
        h = str(self.p.getTime())
        h = h.split(' ', 2)

        self.assertEqual(h[1], '12:34:00')  # sprawdzenie ustawienia godziny na 12:34


class TestInsertMoney(TestParkMeter):
    """
    Klasa testów wrzucania monet
    """
    def testInsert2_4_5_5PLN(self):  # test 2.
        """
        Test polegający na wrzuceniu 2,4,5,5 zł,
        sprawdza po każdym dodaniu czy termin wyjazdu zaktualizował się poprawnie.
        """
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
        """
        Test polegający na wrzuceniu tylu monet aby przejść na koleny dzień z terminem wyjazdu,
        czyli termin wyjazdu powinien być większy od akt. czasu o 12h + wartość wrzuconych monet
        """
        self.p.setTime('2021', '5', '24', 17, 30, 0)
        self.p.addCoin(2, 3)
        self.p.addCoin(5, 1)

        self.assertEqual(self.p.getTime() + timedelta(hours=15), self.p.getLeaveTime())
        # 12h ponieważ parkomat nieczynny od 20 do 8 oraz 3h za wrzucenie 11 zł

    def testInsertUntilNextWeek(self):  # test 4.
        """
        Test polegający na wrzuceniu tylu monet aby przejść na kolejny tydzień,
        analogicznie do poprzedniego testu termin wyjazdu powinien być większy od akt. czasu o
        12h(20:00-8:00) + 48h(sb,nd) + wartość wrzuconych monet
        """
        self.p.setTime('2021', '5', '21', 17, 30, 0)
        self.p.addCoin(2, 3)
        self.p.addCoin(5, 1)

        self.assertEqual(self.p.getTime() + timedelta(hours=63), self.p.getLeaveTime())
        # 12h ponieważ parkomat nieczynny od 20 do 8 oraz 3h za wrzucenie 11 zł oraz 48h za pominięcie weekendu

    def testInsert1PLN(self):  # test 5.
        """
        Test polegający na wrzuceniu złotówki, oczekiwany termin wyjazdu większy o pół godziny od akt. czasy
        """
        self.p.setTime('2021', '5', '21', 17, 30, 0)
        self.p.addCoin(1, 1)

        self.assertEqual(self.p.getTime() + timedelta(minutes=30), self.p.getLeaveTime())
        # 1zł = połowa pierwszej godziny

    def testInsert200GR(self):  # test 6.
        """
        Test polegający na wrzuceniu 200 groszy, oczekiwany termin wyjazdu większy o godzinę od akt. czasu
        """
        self.p.setTime('2021', '5', '21', 13, 30, 0)
        self.p.addCoin(0.01, 200)

        self.assertEqual(self.p.getTime() + timedelta(hours=1), self.p.getLeaveTime())
        # 2zł = pierwsza godzina

    def testInsert201GR(self):  # test 7.
        """
        Test polegający na wrzuceniu 201 groszy, oczekiwany komunikat o prośbie wrzucenia innego nomianału,
        aktualny czas powinien być równy terminowi wyjazdu
        """
        self.p.setTime('2021', '5', '21', 13, 45, 0)

        self.assertEqual(self.p.addCoin(0.01, 201), "Proszę o wrzucenie innego nominału")  # komunikat
        self.assertEqual(self.p.getLeaveTime(), self.p.getTime())  # obecny czas i termin wyjazdu są sobie równe


class TestConfirmPress(TestParkMeter):
    """
    Klasa testów wciśnięcia przycisku zatwierdź
    """
    def testConfirmWithoutMoneyInserted(self):  # test 8.
        """
        Test polegający na wciśnięciu przycisku zatwierdź bez wrzucania monet do parkomatu,
        oczekiwany komunikat o tym, że nie wrzucono żadnych monet
        """
        self.assertEqual(self.p.confirmPress('KLI993X'), "Nie wrzucono żadnych monet")  # komunikat

    def testConfirmWithoutRegistrationPlate(self):  # test 9.
        """
            Test polegający na wciśnięciu przycisku zatwierdź z niepoprawną rejestracją,
            oczekiwany komunikat o tym, że rejestracja jest niepoprawna
        """
        self.p.addCoin(0.01, 1)

        self.assertEqual(self.p.confirmPress('@l9fd'), "Niepoprawna rejestracja")  # komunikat

    def testConfirmWithoutMoneyAndRegistration(self):  # połączenie testu 8. i 9.
        """
        Test polegający na wciśnięciu przycisku zatwierdź z niepoprawną rejestracją oraz bez wrzucania monet
        do parkomatu oczekiwany komunikat o tym, że rejestracja jest niepoprawna oraz nie wrzucono żadnych monet
        """
        self.assertEqual(self.p.confirmPress(''),
                         "Niepoprawna rejestracja oraz nie wrzucono żadnych monet")  # komunikat


if __name__ == '__main__':
    unittest.main()
