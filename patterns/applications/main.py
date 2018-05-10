class Screen:

    def display(self, image):
        print('Displaying "{}"'.format(image))


class Speaker:

    def play(self, sound):
        print('Playing "{}"'.format(sound))


class HardDrive:

    def write(self, data):
        print('Writing "{}" to disk'.format(data))


class Applications(dict):

    def __setitem__(self, name, app):
        try:
            self.__getitem__(name)
            raise PermissionError('App "{name}" is already installed!'.format(name=name))
        except KeyError:
            super(Applications, self).__setitem__(name, app)


class Computer:

    def __init__(self):
        self.screen = Screen()
        self.speaker = Speaker()
        self.disk = HardDrive()
        self.apps = Applications()

    def install_app(self, installer, *args, **kwargs):
        app = installer(self, *args, **kwargs)
        app.install()

    def __getattr__(self, item):
        try:
            return self.apps[item]
        except KeyError:
            pass


class App(object):

    name = None

    def __init__(self, computer):
        self.computer = computer

    def install(self):
        self.computer.apps[self.name] = self


class PdfReader(App):

    name = 'pdf_reader'

    def install(self):
        super(PdfReader, self).install()
        self.computer.disk.write('pdf reader data')

    def read_document(self, document):
        self.computer.screen.display(document)


class VideoPlayer(App):

    name = 'video_player'

    def install(self):
        super(VideoPlayer, self).install()
        self.computer.disk.write('video player data')

    def play_video(self, video):
        self.computer.screen.display(video)
        self.computer.speaker.play(video)


if __name__ == '__main__':
    home_pc = Computer()
    home_pc.install_app(PdfReader)
    home_pc.install_app(VideoPlayer)
    home_pc.pdf_reader.read_document('Harry_Potter.pdf')
    home_pc.video_player.play_video('Pulp_Fiction.mp4')
