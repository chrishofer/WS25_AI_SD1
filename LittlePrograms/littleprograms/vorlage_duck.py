class Duck:
    def quack(self):
        print("quack quack")

    def fly(self):
        print("Flies through the sky")


class WoodDuck:
    def quack(self):
        print("*silence*")

    def fly(self):
        print("Gets thrown")


class Human:
    def quack(self):
        print("*awkward silence* *quack quack*")

    def fly(self):
        print("*ouch*")

class Cat:
    pass

if __name__ == '__main__':
    d = Duck()
    w = WoodDuck()
    h = Human()
    c = Cat()

    # uberpruefen ob eine methode existiert
    # (normalerweise solte man es über vererbung umsetzteh, aber mit der funktion ist es nicht ganz so "gefährlich")
    print(hasattr(c, 'quack'))

    # unterschiedliche objekte (keine Vererbungshierarchie)
    ducks = [d, w, h, c]

    # duck typing
    for duckling in ducks:
        if hasattr(duckling, 'quack'):
            duckling.quack()
        else:
            print("Missing quack method")
        if hasattr(duckling, 'fly'):
            duckling.fly()
        else:
            print("Missing fly method")
        print("---")
