from karte import Karte
class Hand:
    def __init__(self, karten, spielernummer):
        self.karten = karten
        self.spielernummer = spielernummer
    def getKarten(self):
        return self.karten
    def getspielernummer(self):
        return self.spielernummer
    def __str__(self):
        text = "Spieler: " + str(self.spielernummer) + "\n"
        for nummer, karten in enumerate(self.karten):
             text +=  str(nummer) + ": " + str(karten) + "\n"
        return text
        