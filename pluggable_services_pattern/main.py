from lab import Server
from lab import CustomServer


def test_server(server):
    server.set_up_ssh()
    system_info = server.get_system_info()
    print(system_info)
    disk_space = server.get_disk_space()
    print(disk_space)


if __name__ == '__main__':
    node = 'node_7'

    regular_server = Server('my_server', default_ssh_node=node)
    print('--- Testing regular server ---')
    test_server(regular_server)

    custom_server = CustomServer('my_custom_server', default_ssh_node=node)
    print('--- Testing custom server ---')
    test_server(custom_server)
