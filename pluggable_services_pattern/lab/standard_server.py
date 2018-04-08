from lab.ssh.mixins import MultipleSshMixin


class Server(MultipleSshMixin):

    def __init__(self, model, default_ssh_node=None):
        self.model = model
        self.default_ssh_node = default_ssh_node
        self.ssh_connections = {}
        print('Created new server: "{}"'.format(self.model))

    def get_system_info(self, node=None):
        command = 'uname -a'
        return self.run_ssh_command(command, node=node)

    def get_disk_space(self, node=None):
        command = 'df'
        return self.run_ssh_command(command, node=node)
