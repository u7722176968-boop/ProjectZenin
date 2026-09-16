from karte import Karte
class Stapel:
    def __init__(self):
        self.verdeckt = []
        self.abgelegt = []
    def StapelErzeugen(self):
        for i in range(2):
            for i in range(10):
                karte = Karte("blau", i)
                self.verdeckt.append(karte)
            for i in range(10):
                karte = Karte("grün", i)
                self.verdeckt.append(karte)
            for i in range(10):
                karte = Karte("rot", i)
                self.verdeckt.append(karte)
            for i in range(10):
                karte = Karte("gelb", i)
                self.verdeckt.append(karte)
    def getVerdeckt(self):
        return self.verdeckt
    def getAbgelegt(self):
        return self.abgelegt
    def setVerdeckt(self, karten):
        self.verdeckt = karten
    def setAbgelegt(self, karten):
        self.abgelegt = karten
    def verdecktToString(self):
        text = "verdeckt:\n"
        for karte in self.verdeckt:
            text += str(karte) + "\n"
        print(text)

stapel1 = Stapel()
karte1 = Karte("blau", 0)
karte2 = Karte("rot", 6)
karte3 = Karte("grün", 4)

karten = [karte1, karte2, karte3]
stapel1.setVerdeckt(karten)
stapel1.verdecktToString()