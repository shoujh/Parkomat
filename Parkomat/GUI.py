from tkinter import *
from ParkingMeter import *


class gui:
    _amount = 0
    _value = 0.0
    _plate = ''

    def interface(self):
        p = ParkingMeter()
        window = Tk()
        window.title("Parkomat")
        t = StringVar()
        t.set(p.getTime())
        Label(window, textvariable=t).pack()
        print(t.get())
        inputamount = Text(window, height=1, width=25)
        inputplate = Text(window, height=1, width=25)

        def coinInsert(value):
            setattr(self, '_value', value)
            setattr(self, '_amount', inputamount.get(1.0, END)),
            setattr(self, '_plate', inputplate.get(1.0, END)),
            print(p.addCoin(float(self._value), int(self._amount), self._plate))

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
        setdate = Button(window, height=2, width=20, text="Zmiana Daty", command=lambda: t.set(p.getLeaveTime()))
        confirm = Button(window, height=2, width=20, text="Zatwierdź", command=lambda: print(p.getTicket()))

        inputamount.pack()
        inputplate.pack()
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
        setdate.pack()
        confirm.pack()
        window.mainloop()
