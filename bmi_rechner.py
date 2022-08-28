# Datei:    bmi_rechner.py
# Version:  1.0
# Autor:    Th.Beyer

class BMI_Rechner:
    def __init__(self):
        self.masse = 0.0
        self.groesse = 0.0
        self.bmi = 0.0
        self.geschlecht = ""

    def setMasse(self, m):
        self.masse = m

    def setGroesse(self, g):
        self.groesse = g

    def setGeschlecht(self, ge):
        self.geschlecht = ge

    def getGeschlecht(self):
        return self.geschlecht

    def getBmi(self):
        return self.bmi

    def calculateBmi(self):
        self.bmi = self.masse / (self.groesse * self.groesse)

    def getBmiBeurteilung(self):
        if self.bmi <= 20 and self.geschlecht == "m":
            return "Untergewicht"
        elif 20 < self.bmi <= 25 and self.geschlecht == "m":
            return "Normalgewicht"
        elif 25 < self.bmi <= 30 and self.geschlecht == "m":
            return "Ubergewicht"
        elif 30 < self.bmi <= 40 and self.geschlecht == "m":
            return "Adipositas"
        elif self.bmi >= 40 and self.geschlecht == "m":
            return "massive Adipositas"

        if self.bmi <= 19 and self.geschlecht == "w":
            return "Untergewicht"
        elif 19 < self.bmi <= 24 and self.geschlecht == "w":
            return "Normalgewicht"
        elif 24 < self.bmi <= 30 and self.geschlecht == "w":
            return "Ubergewicht"
        elif 30 < self.bmi <= 40 and self.geschlecht == "w":
            return "Adipositas"
        elif self.bmi >= 40 and self.geschlecht == "w":
            return "massive Adipositas"
