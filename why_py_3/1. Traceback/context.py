from some_harmless_module import some_harmless_function, typical_cleanup


class Fridge:

    def __init__(self):
        self.open = False

    def __enter__(self):
        self.open = True
        return self

    def sing_a_song(self):
        some_harmless_function()
        print('I am a fridge, lalala, what a song, OMG')

    def __exit__(self, exc_type, exc_val, exc_tb):
        typical_cleanup()
        self.open = False


with Fridge() as fridge:
    fridge.sing_a_song()

