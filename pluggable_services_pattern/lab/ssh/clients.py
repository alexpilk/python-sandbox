class StandardSshClient:

    def __init__(self):
        self.running = False

    def create_connection(self):
        self.running = True

    def execute_command(self, command):
        print('Executing "{}"'.format(command))
        return '"{}" execution output'.format(command)

    def disconnect(self):
        self.running = False


class NewSshClient:

    def __init__(self):
        self.connection = False

    def connect(self):
        self.connection = True

    def run_command(self, command):
        print('Running "{}"'.format(command))
        return '"{}" output'.format(command)

    def disconnect(self):
        self.connection = False
