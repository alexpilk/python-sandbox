from lab.ssh.clients import NewSshClient
from lab.ssh.services import SshService
from lab import Server


class CustomSshService(SshService):

    default_client = NewSshClient

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
