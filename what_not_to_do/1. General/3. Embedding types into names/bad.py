class Egg:

    def __init__(self):
        self.smashed = False

    def smash(self):
        self.smashed = True


# Python is not a statically typed language!
# Don't make it look like it is by adding types to names!
# Use type hints and docstrings if you need to
def smash_eggs(egg_list):
    for egg in egg_list:
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
        return self


# But if an EggContainer is passed, `egg_list` is no longer an appropriate name.
# This demonstrates how embedding types into variable names leads to confusion.
my_eggs = EggContainer(Egg(), Egg(), Egg())
smash_eggs(my_eggs)
