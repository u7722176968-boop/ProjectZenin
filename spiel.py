from hand import Hand
from stapel import Stapel


class Spiel:
    def __init__(self):
        self.spieler = []
        self.stapel = Stapel()
    def karteblegen(self,l, legendeKarte):
        self.gelegteKarte = self.spieler[l-1].getKarten().pop(legendeKarte)
        
        print("Gelegte Karte:")
        print(self.gelegteKarte)
        
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
            print(self.spieler[l-1])

            eingabe = input()

            if eingabe.lower() == "ja":

                print("Position der zu legenden Karte eingeben:")
                legendeKarte = int(input())

                if 0 <= legendeKarte < len(self.spieler[l-1].getKarten()):

                    karte = self.spieler[l-1].getKarten()[legendeKarte]

                    if self.kartePruefen(karte):
                        self.karteblegen(l, legendeKarte)

                        l += 1

                        if l > self.spieleranzahl:
                            l = 1

                    else:
                        print("Diese Karte ist nicht legbar!")

                else:
                    print("Gib eine Position ein, die in deinem Kartendeck vorhanden ist!")

            elif eingabe.lower() == "passen":
                l += 1

                if l > self.spieleranzahl:
                    l = 1

    def spielen(self):
        self.stapel.StapelErzeugen()
        self.stapel.mischen(0)

        print("Spieleranzahl eingeben: ")
        self.spieleranzahl = int(input())

        self.spieler = self.stapel.ausgeben(self.spieleranzahl)

        print("Zum Anzeigen der UNO-Hand weiter eingeben: ")
        eingabe = input()
        k = 0

        while True:

            if eingabe == "weiter":
                if k < self.spieleranzahl:
                    print(self.spieler[k])
                    k = k + 1
                else:
                    print("Alle Hände angezeigt.")
                    print("Für Spielbeginn: starten : eingeben")

            elif eingabe == "starten":
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

        
        
        