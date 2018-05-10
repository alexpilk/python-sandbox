from lab.server import Server
from custom_lab import CustomServer


def test_server(server):
    server.set_up_ssh()
    system_info = server.get_system_info()
    print(system_info)
    disk_space = server.get_disk_space()
    print(disk_space)


if __name__ == '__main__':
    node = 'node_7'

    print('--- Regular server example ---')
    with Server('my_server', default_ssh_node=node) as my_server:
        test_server(my_server)

    print('--- Regular server example ---')
    with CustomServer('custom_server', default_ssh_node=node) as custom_server:
        test_server(custom_server)
