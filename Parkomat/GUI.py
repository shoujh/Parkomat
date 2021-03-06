from tkinter import *
from ParkingMeter import *


class gui:
    """
    Klasa interfejsu

    Przechowuje ilość wrzucanych monet, nominał wrzucanej monety, tablice rejestracyjną oraz datę.
    """
    _amount = 0
    _value = 0.0
    _plate = ''
    _date = ''

    def popup_window(self, p):
        """
        Metoda odpowiadająca za oknapopup
        :param p: tekst wyświetlany w oknie popup
        """
        window = Toplevel()

        label = Label(window, height=2, text=p)
        label.pack()

        button_close = Button(window, text="Zamknij", command=window.destroy)
        button_close.pack(fill='x')

    def interface(self):
        """
        Metoda odpowiedzialna za utworzenie obiektu Parkomat oraz funkcjonowanie interfejsu
        """
        p = ParkingMeter()
        window = Tk()
        window.title("Parkomat")
        t = StringVar()
        tl = StringVar()
        t.set("Aktualna data: {}".format(p.getTime()))
        tl.set("Termin wyjazdu {}".format(p.getLeaveTime()))
        Label(window, height=2, textvariable=t).pack()
        Label(window, height=2, textvariable=tl).pack()
        input_amount = Text(window, height=1, width=25)
        input_plate = Text(window, height=1, width=25)
        input_time = Text(window, height=1, width=25)

        def coinInsert(value):
            """
            Funkcja interfejsu wrzucania monet, ilość pobierana z pola tekstowego, nominał przekazywany w funkcji

            :param value: nominał
            """
            check = True
            setattr(self, '_value', value)
            try:
                setattr(self, '_amount', input_amount.get(1.0, END))
                check = p.checkCoin(float(self._value), int(self._amount))
                print(p.addCoin(float(self._value), int(self._amount)))
                tl.set("Termin wyjazdu {}".format(p.getLeaveTime()))
            except:
                print("Błędna ilość monet")
            if not check:
                self.popup_window("Proszę o wrzucenie innego nominału")

        def changePresentDate():
            """
            Funkcja interfejsu zmieniająca bieżącą datę na wprowadzoną w pole tekstowe (yyyy mm dd hh mm ss),
            """
            setattr(self, '_date', input_time.get(1.0, END))
            self._date = self._date.split(" ", 5)
            try:
                p.setTime(self._date[0], self._date[1], self._date[2], int(self._date[3]), int(self._date[4]),
                          int(self._date[5]))
                t.set("Aktualna data: {}".format(p.getTime()))
                tl.set("Termin wyjazdu {}".format(p.getLeaveTime()))
            except:
                return "Niepoprawna data lub godzina"
            return "Zaktualizowano czas"

        def Confirm():
            """
            Funkcja interfejsu zatwierdzająca wydanie biletu, rejestracja pobierana z pola tekstowego
            """
            setattr(self, '_plate', input_plate.get(1.0, END))
            self.popup_window(p.confirmPress(self._plate))
            tl.set("Termin wyjazdu {}".format(p.getLeaveTime()))

        # przyciski oraz pola
        coin001 = Button(window, height=2, width=25, text="1gr", command=lambda: coinInsert(0.01))
        coin002 = Button(window, height=2, width=25, text="2gr", command=lambda: coinInsert(0.02))
        coin005 = Button(window, height=2, width=25, text="5gr", command=lambda: coinInsert(0.05))
        coin010 = Button(window, height=2, width=25, text="10gr", command=lambda: coinInsert(0.1))
        coin020 = Button(window, height=2, width=25, text="20gr", command=lambda: coinInsert(0.2))
        coin050 = Button(window, height=2, width=25, text="50gr", command=lambda: coinInsert(0.5))
        coin100 = Button(window, height=2, width=25, text="1zł", command=lambda: coinInsert(1))
        coin200 = Button(window, height=2, width=25, text="2zł", command=lambda: coinInsert(2))
        coin500 = Button(window, height=2, width=25, text="5zł", command=lambda: coinInsert(5))
        coin1000 = Button(window, height=2, width=25, text="10zł", command=lambda: coinInsert(10))
        coin2000 = Button(window, height=2, width=25, text="20zł", command=lambda: coinInsert(20))
        coin5000 = Button(window, height=2, width=25, text="50zł", command=lambda: coinInsert(50))
        setdate = Button(window, height=3, width=20, text="Zmiana Daty", command=lambda: print(changePresentDate()))
        confirm = Button(window, height=3, width=20, text="Zatwierdź", command=lambda: Confirm())
        button_close = Button(window, height=3, width=20, text="Zamknij", command=window.destroy)

        Label(window, text="Ilość:").pack()
        input_amount.pack()
        Label(window, text="Rejestracja:").pack()
        input_plate.pack()
        Label(window, text="Zmiana czasu:").pack()
        input_time.pack()
        setdate.pack()
        coin001.pack()
        coin002.pack()
        coin005.pack()
        coin010.pack()
        coin020.pack()
        coin050.pack()
        coin100.pack()
        coin200.pack()
        coin500.pack()
        coin1000.pack()
        coin2000.pack()
        coin5000.pack()
        confirm.pack()
        button_close.pack()
        window.mainloop()
