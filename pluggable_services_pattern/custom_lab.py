from lab.server import Server
from lab.ssh.service import SshService


class CustomSshClient:

    def __init__(self):
        self.connection = False

    def connect(self):
        self.connection = True
        print('SSH connected')

    def run_command(self, command):
        print('Running "{}"'.format(command))
        return '"{}" output'.format(command)

    def disconnect(self):
        self.connection = False
        print('SSH disconnected')


class CustomSshService(SshService):

    default_client = CustomSshClient

    @property
    def active(self):
        return self._client.connection is True

    def start(self):
        self._client.connect()


class CustomServer(Server):

    default_ssh_service = CustomSshService

    def run_ssh_command(self, command, node=None):
        node = self.get_ssh_node(node)
        service = self.ssh_connections[node]
        return service.client.run_command(command)
