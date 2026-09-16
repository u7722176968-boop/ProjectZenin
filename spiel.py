from hand import Hand
#from stapel import Stapel


class Spiel:
    def __init__(self):
            #self.Stapel = Stapel
            self.spieler = []
    def spielen(self):
            print("Spieleranzahl eingeben: ")
            i = input()
            for x in range(int(i)):
                hand = Hand([], x+1)
                self.spieler.append(hand)
            print(self.spieler)
Spiel = Spiel()
Spiel.spielen()
        
        
        