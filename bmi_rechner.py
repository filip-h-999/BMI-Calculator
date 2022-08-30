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
        try:
            self.bmi = self.masse / (self.groesse * self.groesse)
        except:
            print("Keine Daten eingegeben")

    def getBmiBeurteilung(self):
        if self.geschlecht == "m":
            if self.bmi <= 20:
                return "Untergewicht"
            elif 20 < self.bmi <= 25:
                return "Normalgewicht"
            elif 25 < self.bmi <= 30:
                return "Ubergewicht"
            elif 30 < self.bmi <= 40:
                return "Adipositas"
            elif self.bmi >= 40:
                return "massive Adipositas"

        if self.geschlecht == "w":
            if self.bmi <= 19:
                return "Untergewicht"
            elif 19 < self.bmi <= 24:
                return "Normalgewicht"
            elif 24 < self.bmi <= 30:
                return "Ubergewicht"
            elif 30 < self.bmi <= 40:
                return "Adipositas"
            elif self.bmi >= 40:
                return "massive Adipositas"
