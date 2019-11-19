

class Car(object):

    def start(self):
        print('Engine start')


class RaceCar(Car):

    def start(self):
        print('Preparing nitro')
        super(RaceCar, self).start()


class FlyingRaceCar(RaceCar):

    def start(self):
        print('Preparing wings')
        super(RaceCar, self).start()


FlyingRaceCar().start()
