class Drink:
    def __init__(self, name:str, volume:float, temp:float, nr_ice_cubes: int, alcohol_perc:float):
        self.alcohol_perc = alcohol_perc
        if self.alcohol_perc > 0:
            self.is_alcoholic = True
        else:
            self.is_alcoholic = False

        self.nr_ice_cubes = nr_ice_cubes
        self.temp = temp
        self.volume = volume
        self.name = name
    def __repr__(self):
        return f'Drink(name={self.name})'

    def drink(self):
        self.volume = 0

if __name__ == '__main__':
    d1 = Drink("Hansi's Beer", 500, 7, 0, 0.051)
    print(d1)
    print(d1.volume)
    d1.drink()
    print(d1.volume)





