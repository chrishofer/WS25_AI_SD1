class Hund: # Namen mit CamelCase (Bsp. HundMitKatze)
    species = "Canis lupus familiaris" # Klassenattribut (oder auch statisches Attribut genannt)


    # init Methode wird aufgerufen wenn neues Objekt erzeugt wird
    def __init__(self, n: str, a: int):
        self.name = n # Parameter n wird auf Instanzattribut name gespeichert (Jedes Objekt/Instanz hat eigene Version davon)
        self.age = a
        # hier könnten wir andere Methoden aufrufen die sehr komplizierte Sacheb machen

    def gib_laut(self, text:str):
        print(f'{self.name} bellt ganz laut {text}')

    def __str__(self):
        return f'Der Hund {self.name} ist bereits {self.age} Jahre alt'

    def __repr__(self):
        return f'Hund(name={self.name}, age={self.age})'

class Katze:
    pass

if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 14)
    lassie = Hund("Lassie", 12)

    # Zugriff auf Klassenattribut
    print(Hund.species)
    print(Hund.__dict__)

    # Zugriff auf Instanzattribut
    #print(Hund.age) # das geht nicht - warum?
    print(rex.age)  # Für Zugriff auf Instanzattribute ist immer ein Objekt der Klasse notwendig
    print(lassie.age)


    # Wie rufen wir Methode auf?
    lassie.gib_laut("Ich möchte Menschen retten")

    # Hund ausgeben
    print(lassie)


    # Python verwendet den Inhalt von __dict__ um nachzusehen ob das Attribut/Methode rechts vom . wirklich im Objekt drinnen ist
    # Fall es Python nicht im Objekt selbst findet sucht es in der Klasse des Objekts weiter (Hund.__dict__)
    print(rex.__dict__)
    # Wir können auch auf Klassenattribute über das Objekt selbst zugreifen (aber nur LESEND - wichtig!!!)
    print(rex.species)

    # was passiert wenn wir das nur LESEND oben ignorieren?
    # (das sollte man nicht machen)
    lassie.species = "Kaetzchen" # wir fügen dadurch dem lassie Objekt ein neues Instanzattribut hinzu
    print(lassie.__dict__)

    # Take home message: Auf Klassenattribute immer über Klassennamen zugreifen (so bekannt)
    # Instanzattribute über Instanz zugreifen

