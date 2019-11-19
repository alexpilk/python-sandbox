

class Car:

    def start(self):
        print('Engine start')


class RaceCar(Car):

    def start(self):
        print('Preparing nitro')
        super().start()


RaceCar().start()
