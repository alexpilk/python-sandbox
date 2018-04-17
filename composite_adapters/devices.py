from adapters import CompositeAdapter, SshAdapter, CustomSshAdapter


class SimpleDevice(object):

    def __init__(self, model):
        self.model = model
        self.ssh_service = SshAdapter()
        print('Created new device: "{}"'.format(self.model))

    def set_up_ssh(self, *args, **kwargs):
        self.ssh_service.set_up_client(*args, **kwargs)

    def get_system_info(self):
        command = 'uname -a'
        output = self.ssh_service.execute_command(command)
        print('Got output: {}'.format(output))

    def get_disk_space(self):
        command = 'df'
        output = self.ssh_service.execute_command(command)
        print('Got output: {}'.format(output))

    def shut_down(self):
        self.ssh_service.stop()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shut_down()


class PatchedDevice(SimpleDevice):

    def __init__(self, *args, **kwargs):
        super(PatchedDevice, self).__init__(*args, **kwargs)
        self.ssh_service = CustomSshAdapter()


class ComplexDevice(object):

    def __init__(self, model, system_node, data_node):
        self.system_node = system_node
        self.data_node = data_node
        self.model = model
        self.ssh_service = CompositeAdapter(SshAdapter)
        print('Created new device: "{}"'.format(self.model))

    def set_up_ssh(self, node=None, *args, **kwargs):
        self.ssh_service[node].set_up_client(*args, **kwargs)

    def get_system_info(self):
        command = 'uname -a'
        output = self.ssh_service[self.system_node].execute_command(command)
        print('Got output: {}'.format(output))

    def get_disk_space(self):
        command = 'df'
        output = self.ssh_service[self.data_node].execute_command(command)
        print('Got output: {}'.format(output))

    def shut_down(self):
        self.ssh_service.stop_all()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shut_down()
