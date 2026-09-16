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
        karteblau = Karte("blau", 0)
        kartegrün = Karte("grün", 0)
        karterot = Karte("rot", 0)
        kartegelb = Karte("gelb", 0)
        self.verdeckt.append(karteblau)
        self.verdeckt.append(kartegrün)
        self.verdeckt.append(karterot)
        self.verdeckt.append(kartegelb)
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
stapel1.StapelErzeugen()
stapel1.verdecktToString()