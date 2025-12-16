class Hund: # Namen mit CamelCase (Bsp. HundMitKatze)
    species = "Canis lupus familiaris" # Klassenattribut (oder auch statisches Attribut genannt)
    anzahl_hunde = 0 # Zählen wie viele Hundeobjekte es gibt

    # Jeder Hund hat eine Chip Nr - diese soll im Nachhinein nicht mehr verändert werden können
    # Machen ein property ohne setter - damit wird die Zuweisung verhindert
    @property
    def chip_nr(self):
        return self.__chip_nr

    # ich möchte jetzt dafür sorgen, dass man age lesen kann und auch verändern kann
    # aber nur positive Werte sollen möglich sein
    @property
    def age(self):
        return self.__age # Speichern unser tatsächliches Alter auf einer privaten Variable damit kein direkter Zugriff möglich ist

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value



    # init Methode wird aufgerufen wenn neues Objekt erzeugt wird
    def __init__(self, n: str, a: int, c:str):
        self.name = n # Parameter n wird auf Instanzattribut name gespeichert (Jedes Objekt/Instanz hat eigene Version davon)

        # Warum verwenden wir bei age nicht __ und bei chip_nr schon?
        # Hier gibt es eine set Methode - wir könneb auch mit __age zugreifen? ABer dann würde es nicht
        # über die set Methode gehen -> wir könnten netgativen Wert zuweisen
        self.__age = a

        # wir müssen auf die private Variable zugreifen, da es ja keine set Methode gibt
        self.__chip_nr = c # Jeder Hund erhält eindeutige chip nummer

        Hund.anzahl_hunde = Hund.anzahl_hunde + 1
        # hier könnten wir andere Methoden aufrufen die sehr komplizierte Sacheb machen

    def gib_laut(self, text:str):
        print(f'{self.name} bellt ganz laut {text}')

    @classmethod # Bezieht sich auf Methode/Funktion/Klasse darunter - Decorator
    def print_anzahl_hunde(cls):
        # cls ist Referenz auf die Klasse (also Hund) - nicht auf die Instanz wie bei self
        # In einer Klassenmethode kann man nur auf Klassenattribute zugreifen
        print(f'Derzeit gibt es {cls.anzahl_hunde} Hunde')


    def __str__(self):
        return f'Der Hund {self.name} ist bereits {self.age} Jahre alt'

    def __repr__(self):
        return f'Hund(name={self.name}, age={self.age})'

    def __del__(self):
        Hund.anzahl_hunde -= 1


class Corgi(Hund):
    def __init__(self, n: str, a: int, c:str, iq:int):
        # Hier machen wir unsere Initialisierung - wir müssen explizit das init unserer Basisklasse aufrufen
        # (Damit die Initialisierung aus Hund durchgeführt wird und wir das nicht erneut umsetzten müssen)
        # die nicht so schöne Variante:
        # Hund.__init__(self, n, a, c)
        # die schöne Variante
        super().__init__(n, a, c)
        self.iq = iq

    def gib_laut(self, text:str):
        print(f'{self.name} besitzt {self.iq} Punkte und bellt etwas weniger laut und rücksichtsvoll {text}')



if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 14, "ABC1234")
    lassie = Hund("Lassie", 12, "XYZ2343434")
    c = Corgi("Cheddar", 12, "99", 150)
    c.gib_laut("Achtung achtung!")
    print(c)

