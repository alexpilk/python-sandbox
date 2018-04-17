# Pluggable services pattern
## Structure
### Clients
Let's say you have a server you want to manage.
For this purpose you create `lab.server.Server` class.
You want to be able to connect to this server via SSH.
For this you need `lab.ssh.client.SshClient`.
Our imaginary client has the following methods: `create_connection`, `execute_command` and `disconnect`.
To use it inside `Server` class you could create an ssh client attribute.
### Services
But here is the problem: what if your `Server` class gets really big and only a few methods will need SSH?
In this case - you don't know if the `Server` user needs SSH, so opening an SSH connection in `__init__` would be wasteful.
The solution is to wrap the client into `@property` decorator and check if the connection is open every time someone tries to access the client.
This way you can automatically open a connection whenever someone uses a method that requires SSH.
But it can be improved further. Most probably your server will also use VNC, telnet and other stuff.
You don't want to flood your `Server` class with methods for checking, opening and stopping connections.
To avoid it - we can wrap the property with all SSH connection-related methods into the `Service` class.
Now, in your `Server` you can have a `self.ssh_service` attribute. Then you can access the client property like this: `self.ssh_service.client`.
### Mixins
Here are a few problems with this approach:
1. You code gets really long e.g. `self.ssh_service.ssh_client.execute_command`
2. You expose the client in the Server class.
If you have 10 methods which use SSH and then you want to switch to another SSH client which uses `run_command` instead of `execute_command` - you will need to override 10 methods.

To avoid it, mixins can be used. You can create your own `run_ssh_method` in the mixin. This way:
1. Your code gets shorter, because now you can just `self.run_ssh_command`
2. If you want to switch your client and it uses `run_command` instead of `execute_command` - you only have to override `run_ssh_command`.
## Example
The pattern described above is demonstrated in given code example.
- Client: `lab.ssh.clients.SshClient`
- Service: `lab.ssh.service.SshService`
- Mixin: `lab.ssh.MultipleSshMixin`
- Server (end user): `lab.server.Server`
In `custom_lab.py` a new `CustomSshClient` is created.

There you have an example of how to add `CustomSshService` and switch the client in `CustomServer`.
In `main.py` it's demonstrated how both of those servers can be used in the same way regardless of SSH client.
