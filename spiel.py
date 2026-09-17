from hand import Hand
from stapel import Stapel

class Spiel:
    def __init__(self):
        self.spieler = []
        self.stapel = Stapel()
    def spielen(self):
            stapel1 = Stapel()
            stapel1.StapelErzeugen()
            stapel1.mischen(0)
            

            print("Spieleranzahl eingeben: ")
            spieleranzahl = input()
            
            self.spieler = stapel1.ausgeben(int(spieleranzahl))
            print("Zum Anzeigen der UNO-Hand weiter eingeben: ")
            eingabe = input()
            k = 0
            while True:
                if eingabe == "weiter":
                 if int(k) < int(spieleranzahl):
                    print(self.spieler[k])
                    k = k+1
                    eingabe = input()
                 else:
                     print("Alle Hände angezeigt, zum Spiel starten starten eingeben: ")
                     eingabe = input()
                elif eingabe == "starten":
                    break
            print("Spiel geht los")
            



Spiel = Spiel()
Spiel.spielen()
        
        
        