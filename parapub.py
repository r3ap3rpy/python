import paramiko
import os

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('centos', username=os.getenv('PUSER'), key_filename=os.getenv('PPASS'))

stdin, stdout, stderr = client.exec_command('uptime')

print(stdout.readlines())
