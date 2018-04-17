from clients import SshClient, CustomSshClient
from collections import defaultdict


class ClientNotSetUpException(Exception):
    pass


class CompositeAdapter:

    default_name = 'default'

    def __init__(self, adapter):
        self.nodes = defaultdict(adapter)

    def __getitem__(self, node_name=None):
        node_name = node_name or self.default_name
        return self.nodes[node_name]

    def __getattr__(self, attr):
        return getattr(self.nodes[self.default_name], attr)

    def stop_all(self):
        for node in self.nodes:
            self.nodes[node].stop()


class SshAdapter:

    client_factory = SshClient

    def __init__(self):
        self._client = None

    def set_up_client(self, *args, **kwargs):
        self._client = self.client_factory(*args, **kwargs)

    def start(self):
        self._client.create_connection()

    def stop(self):
        self._client.disconnect()

    @property
    def ready(self):
        return self._client is not None

    @property
    def active(self):
        return self._client.running is True

    @property
    def client(self):
        if not self.ready:
            raise ClientNotSetUpException()
        if not self.active:
            self.start()
        return self._client

    def execute_command(self, command):
        return self.client.execute_command(command)


class CustomSshAdapter(SshAdapter):

    client_factory = CustomSshClient

    @property
    def active(self):
        return self._client.connection is True

    def start(self):
        self._client.connect()

    def execute_command(self, command):
        return self._client.run_command(command)
