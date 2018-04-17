from .client import SshClient


class ClientNotSetUpException(Exception):
    pass


class SshService:

    default_client = SshClient

    def __init__(self):
        self._client = None

    def set_up_client(self, *args, **kwargs):
        self._client = self.default_client(*args, **kwargs)

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
