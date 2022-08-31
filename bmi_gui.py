import math
from tkinter import *
import keyboard
from bmi_rechner import *


class BMI_GUI:

    def __init__(self):
        self.derRechner = BMI_Rechner()

        window = Tk()
        window.geometry("300x300+800+200")
        window.title("BMI-Rechner")
        window.resizable(False, False)

        def createLabel(name: str, posX: int, posY: int, Width: int, Height: int):
            lab = Label(window, fg="black", relief="raised", text=name)
            lab.place(x=posX, y=posY, width=Width, height=Height)

        createLabel("Körpermasse:", 60, 30, 80, 25)
        createLabel("Körpergröße:", 60, 60, 80, 25)
        createLabel("Geschlecht:", 60, 90, 80, 25)
        createLabel("Klassifikation:", 60, 220, 80, 25)
        createLabel("Werte:", 60, 250, 80, 25)
        createLabel("in Kg", 208, 30, 35, 25)
        createLabel("im M", 208, 60, 35, 25)
        createLabel("m/w", 208, 90, 35, 25)

        self.classification = StringVar()
        self.classification.set("")
        lab6 = Label(window, fg="black", relief="raised", textvariable=self.classification)
        lab6.place(x=150, y=220, width=100, height=25)

        self.wert = IntVar()
        self.wert.set(0)
        lab7 = Label(window, fg="black", relief="raised", textvariable=self.wert)
        lab7.place(x=150, y=250, width=100, height=25)

        def createEntry(textvar: DoubleVar(), posX: int, posY: int, Width: int, Height: int, nextFocus: Entry = None):
            text = Entry(window, fg="black", relief="raised", textvariable=textvar)
            text.place(x=posX, y=posY, width=Width, height=Height)
            if nextFocus is not None:
                text.bind("<Down>", lambda funct1: nextFocus.focus())
            return text

        self.gender = StringVar()
        entryGender = createEntry(self.gender, 150, 90, 50, 25)

        self.korpergrosse = DoubleVar()
        entryGrosse = createEntry(self.korpergrosse, 150, 60, 50, 25, entryGender)

        self.korpermasse = DoubleVar()
        entryMasse = createEntry(self.korpermasse, 150, 30, 50, 25, entryGrosse)
        entryMasse.focus()

        btn = Button(window, text="Berechnen", font="courier 12 italic bold", background="lightgreen",
                     command=self.annehmen)
        btn.place(x=100, y=150, width=100, height=40)

        keyboard.on_press_key("Enter", lambda _: self.annehmen())

    def annehmen(self):
        self.datenAktualisieren()
        self.anzeigeAktualisieren()

    def datenAktualisieren(self):
        kMasse = self.korpermasse.get()
        kGrosse = self.korpergrosse.get()
        mwGeschlecht = self.gender.get()

        self.derRechner.setMasse(kMasse)
        self.derRechner.setGroesse(kGrosse)
        self.derRechner.setGeschlecht(mwGeschlecht)
        self.derRechner.calculateBmi()

    def anzeigeAktualisieren(self):
        beurteilung = self.derRechner.getBmiBeurteilung()
        self.classification.set(beurteilung)
        bmi = self.derRechner.getBmi()
        self.wert.set(math.ceil(bmi))


if __name__ == '__main__':
    dasFenster = BMI_GUI()
    mainloop()
