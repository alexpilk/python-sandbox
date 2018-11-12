class Car:

    def __init__(self, wheels):
        self.wheels = wheels

    def drive(self):
        self.wheels.spin()

    def beep(self):
        print('Beep')
