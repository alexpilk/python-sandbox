import os
import re

from paramiko.client import SSHClient

client = SSHClient()
client.load_system_host_keys()

try:
    client.connect(os.environ['LAK_URL'], username=os.environ['LAK_USERNAME'], password=os.environ['LAK_PASSWORD'])
    stdin, stdout, stderr = client.exec_command('ls -l')
    data = stdout.read()
    search_result = re.search(r'\d\d:\d\d \S*', data).group()
    print(search_result)
finally:
    client.close()
