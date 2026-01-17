import abc
import math

# Simulationsobjekt für Tiersimulation
# Da alle Methoden abstrakt sind wäre das sinngemäßig einem Interface in einer anderen Sprache entsprechend
class SimObject(abc.ABC):
    @abc.abstractmethod
    def move(self, x: int, y:int):
        pass

    @abc.abstractmethod
    def attack(self, enemy_list: list):
        pass

    @abc.abstractmethod
    def defend(self, enemy):
        pass




# es gibt auch decorator für abstractstaticmethod und abstractclassmethod
# bei Mehrfachvererbung MUSS abc.ABC als letzte Klasse angegeben werden
class Flaeche(abc.ABC):
    # Alle Klassen die sich von der abstrakten Klasse ableiten müssen diese Methode umsetzten
    @abc.abstractmethod
    def flaeche(self) -> float:
        pass

    # Diese Methoden können von ableitenden Klassen aufgerufen werden
    def winkewinke(self):
        print("winke winke")


class Kreis(Flaeche):
    def flaeche(self) -> float:
        return self.r ** 2 * math.pi
    def __init__(self, r:float):
        self.r = r


class Rechteck(Flaeche):
    def flaeche(self) -> float:
        return self.l * self.b

    def __init__(self, l, b):
        self.l = l
        self.b = b




if __name__ == '__main__':
    # Abstrakte Klassen können nicht instanziert werden (keine Objekte erzeugen)
    # f = Flaeche() # geht nicht
    r = Rechteck(4, 3)
    print(r.flaeche())
    r.winkewinke()



