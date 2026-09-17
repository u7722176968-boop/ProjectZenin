from karte import Karte
from hand import Hand
import random
class Stapel:
    def __init__(self):
        self.verdeckt = []
        self.abgelegt = []
    def StapelErzeugen(self):
        for i in range(2):
            for i in range(9):
                karte = Karte("blau", i+1)
                self.verdeckt.append(karte)
            for i in range(9):
                karte = Karte("grün", i+1)
                self.verdeckt.append(karte)
            for i in range(9):
                karte = Karte("rot", i+1)
                self.verdeckt.append(karte)
            for i in range(9):
                karte = Karte("gelb", i+1)
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
    def setVerdeckt(self, karte):
        self.verdeckt.append(karte)
    def setAbgelegt(self, karte):
        self.abgelegt.append(karte)
    def verdecktToString(self):
        text = "verdeckt:\n"
        for karte in self.verdeckt:
            text += str(karte) + "\n"
    def abgelegtToString(self):
            text = "abgelegt:\n"
            for karte in self.abgelegt:
                text += str(karte) + "\n"
    def mischen(self, stapelnummer):
        if stapelnummer == 0:
            random.shuffle(self.verdeckt)
        else:
            random.shuffle(self.abgelegt)
    def aufdecken(self):
        aufgedeckteKarte = self.verdeckt.pop(0)
        self.abgelegt.append(aufgedeckteKarte)
    def getAnzahl(self, nummer):
        if nummer == 0:
            return len(self.verdeckt)
        else:
            return len(self.abgelegt)
    def ausgeben(self, spieleranzahl):
        haende = []
        for i in range(spieleranzahl):
            verteilteKarten = []
            for _ in range(7):
                karteVerteilung = self.verdeckt.pop(0)
                verteilteKarten.append(karteVerteilung)
            anfangsHand = Hand(verteilteKarten, i+1)
            haende.append(anfangsHand)
        return haende
        
stapel1 = Stapel()
stapel1.StapelErzeugen()
stapel1.verdecktToString()
stapel1.mischen(0)
stapel1.verdecktToString()
stapel1.ausgeben(2)
