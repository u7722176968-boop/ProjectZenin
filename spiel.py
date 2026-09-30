from hand import Hand
from stapel import Stapel
import random
import os


class Spiel:
    def __init__(self):
        self.spieler = []
        self.stapel = Stapel()
    def clear(self):
        os.system("clear")
        print("Ablagestapel:")
        print(self.stapel.abgelegt[-1])
    def karteblegen(self,l, legendeKarte):
        self.gelegteKarte = self.spieler[l-1].getKarten().pop(legendeKarte)
    
        
        self.stapel.setAbgelegt(self.gelegteKarte)
        
        print("Ablagestapel:")
        print(self.stapel.abgelegt[-1])
       
    def kartePruefen(self, karte):
        if karte.farbe == self.stapel.abgelegt[-1].farbe:
            return True

        if karte.wert == self.stapel.abgelegt[-1].wert:
            return True

        return False
    def spielverlauf(self):
        l = 1

        while True:
            print("Kann Spieler " + str(l) + " legen?")
            print("Für das Legen :ja: eingeben")
            print(self.spielername[l-1] + ":")
            print(self.spieler[l-1])

            eingabe = input()

            if eingabe.lower() == "ja":

                print("Position der zu legenden Karte eingeben:")
                legendeKarte = int(input())

                if 0 <= legendeKarte < len(self.spieler[l-1].getKarten()):

                    karte = self.spieler[l-1].getKarten()[legendeKarte]
                    if self.kartePruefen(karte):
                        self.karteblegen(l, legendeKarte)
                        if len(self.spieler[l-1].getKarten()) == 1:
                            print("UNO")
                        elif len(self.spieler[l-1].getKarten()) == 0:
                            print(self.spielername[l-1] + " hat gewonnen!!!")
                            exit()

                        l += 1

                        if l > self.spieleranzahl:
                            l = 1

                    else:
                        print("Diese Karte ist nicht legbar!")

                else:
                    print("Gib eine Position ein, die in deinem Kartendeck vorhanden ist!")
                self.clear()

            elif eingabe.lower() == "passen":
                karte = self.stapel.verdeckt.pop()
                self.spieler[l-1].getKarten().append(karte)
                print("Gezogenen Karte: " , self.spieler[l-1].getKarten()[-1])
                l += 1
                self.clear()

                if l > self.spieleranzahl:
                    l = 1
            else:
                print("Gib entweder Passen oder ja ein!")

    def spielen(self):
        self.stapel.StapelErzeugen()
        self.stapel.mischen(0)

        print("Spieleranzahl eingeben: ")
        self.spieleranzahl = int(input())

        self.spieler = self.stapel.ausgeben(self.spieleranzahl)
        self.spielername = []
        for i in range(self.spieleranzahl):
            name = input("Name von Spieler " + str(i + 1) + ": ")
            if name == "Arnold":
                self.spielername.append("Soft Daddy")
            elif name == "David":
                x = random.randint(0,1)
                if x == 0:
                    self.spielername.append("Kommandant Schoko")
                elif x == 1:
                     self.spielername.append("Q1BombenKlaus")
            elif name == "Mara":
                self.spielername.append("FetteLuntenKifferin")
            elif name == "Leopold":
                 self.spielername.append("unoMeisterMann")
            else:
                self.spielername.append(name)
            


        print("Zum Anzeigen der UNO-Hand weiter eingeben: ")
        eingabe = input()
        k = 0

        while True:

            if eingabe.lower() == "weiter":
                if k < self.spieleranzahl:
                    print(self.spielername[k] + ":")
                    print(self.spieler[k])
                    k = k + 1
                else:
                    print("Alle Hände angezeigt.")
                    print("Für Spielbeginn: starten : eingeben")

            elif eingabe.lower() == "starten":
                print("Spiel geht los")
                self.stapel.aufdecken()
                print(self.stapel.abgelegt[-1])
                break

            else:
                print("Bitte 'weiter' oder 'starten' eingeben.")

            eingabe = input()
            


Spiel = Spiel()
Spiel.spielen()
Spiel.spielverlauf()

        
        
        