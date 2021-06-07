from tkinter import *
from ParkingMeter import *


class gui:  # klasa interfejsu
    _amount = 0
    _value = 0.0
    _plate = ''
    _date = ''

    def popup_window(self, p):  # funkcja tworząca okno popup
        window = Toplevel()

        label = Label(window, height=2, text=p)
        label.pack()

        button_close = Button(window, text="Zamknij", command=window.destroy)
        button_close.pack(fill='x')

    def interface(self):  # funkcja wywołująca interfejs
        p = ParkingMeter()
        window = Tk()
        window.title("Parkomat")
        t = StringVar()
        tl = StringVar()
        t.set("Aktualna data: {}".format(p.getTime()))
        tl.set("Termin wyjazdu {}".format(p.getLeaveTime()))
        Label(window, height=2, textvariable=t).pack()
        Label(window, height=2, textvariable=tl).pack()
        inputamount = Text(window, height=1, width=25)
        inputplate = Text(window, height=1, width=25)
        inputtime = Text(window, height=1, width=25)

        def coinInsert(value):  # funkcja wrzucenia monety, pobiera ilość z pola tekstowego
            check = True
            setattr(self, '_value', value)
            try:
                setattr(self, '_amount', inputamount.get(1.0, END))
                check = p.checkCoin(float(self._value), int(self._amount))
                print(p.addCoin(float(self._value), int(self._amount)))
                tl.set("Termin wyjazdu {}".format(p.getLeaveTime()))
            except:
                print("Błędna ilość monet")
            if not check:
                self.popup_window("Proszę o wrzucenie innego nominału")

        def changePresentDate():  # funkcja zmieniająca bieżącą date na wprowadzoną w pole tekstowe
            setattr(self, '_date', inputtime.get(1.0, END))
            self._date = self._date.split(" ", 5)
            try:
                p.setTime(self._date[0], self._date[1], self._date[2], int(self._date[3]), int(self._date[4]),
                          int(self._date[5]))
                t.set("Aktualna data: {}".format(p.getTime()))
                tl.set("Termin wyjazdu {}".format(p.getLeaveTime()))
            except:
                return "Niepoprawna data lub godzina"
            return "Zaktualizowano czas"

        def Confirm():  # funkcja zatwierdzająca wydanie biletu, rejestracja wprowadzona w pole tekstowe
            setattr(self, '_plate', inputplate.get(1.0, END))
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
        inputamount.pack()
        Label(window, text="Rejestracja:").pack()
        inputplate.pack()
        Label(window, text="Zmiana czasu:").pack()
        inputtime.pack()
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
