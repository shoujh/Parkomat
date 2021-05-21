from tkinter import *


def gui():
    window = Tk()
    window.title("Parkomat")

    label = Label(window, text="Podaj numer rejestracyjny oraz wrzuć monety").pack()
    input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                        highlightthickness=1)
    input_frame.pack(side=TOP)
    window.mainloop()
