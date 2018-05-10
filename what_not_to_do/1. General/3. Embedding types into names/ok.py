class Egg:

    def __init__(self):
        self.smashed = False

    def smash(self):
        self.smashed = True


# Any iterable containing eggs is fine
def smash_eggs(eggs):
    for egg in eggs:
        egg.smash()


# This is fine:
my_eggs = [Egg(), Egg(), Egg()]
smash_eggs(my_eggs)


class EggContainer:

    def __init__(self, *eggs):
        self.eggs = eggs

    def __getitem__(self, item):
        return self.eggs[item]

    def __iter__(self):
        return iter(self.eggs)


# This is also fine
my_eggs = EggContainer(Egg(), Egg(), Egg())
smash_eggs(my_eggs)
