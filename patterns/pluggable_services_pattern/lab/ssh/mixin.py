from .service import SshService


class MultipleSshMixin(object):

    default_ssh_service = SshService

    def get_ssh_node(self, node=None):
        return node or self.default_ssh_node

    def set_up_ssh(self, node=None, *args, **kwargs):
        node = self.get_ssh_node(node)
        self.ssh_connections[node] = self.default_ssh_service()
        self.ssh_connections[node].set_up_client(*args, **kwargs)

    def run_ssh_command(self, command, node=None):
        node = self.get_ssh_node(node)
        service = self.ssh_connections[node]
        return service.client.execute_command(command)

    def stop_ssh(self, node=None):
        node = self.get_ssh_node(node)
        service = self.ssh_connections[node]
        return service.stop()

    def stop_all_ssh_connections(self):
        for node in self.ssh_connections:
            self.ssh_connections[node].stop()
