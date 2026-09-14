class karte:
    def __init__(self, farbe, wert):
        self.farbe = farbe
        self.wert = wert

    def getFarbe(self):
        return self.farbe
    def getWert(self):
        return self.wert
    def setFarbe(self, farbe):
        self.farbe = farbe
    def setWert(self,wert):
        self.wert=wert
    def __str__(self):
        return self.farbe + ", " + self.wert
karte1 = karte("rot", "1")
karte2 = karte("gelb", "0")
print(karte1)
print(karte2)