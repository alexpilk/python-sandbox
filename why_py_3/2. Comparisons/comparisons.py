class Universe:

    def __init__(self):
        self.planets = None

    def big_bang(self):
        self.planets = 9

    def pluto_is_a_planet(self):
        return self.planets > 8


universe = Universe()
# forgot to call big_bang()
print(universe.pluto_is_a_planet())
