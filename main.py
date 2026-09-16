from karte import Karte
from hand import Hand

karte1 = Karte("blau", 0)
karte2 = Karte("rot", 6)
karte3 = Karte("grün", 4)

karten = [karte1, karte2, karte3]

hand1 = Hand(karten, 1)

print(hand1)