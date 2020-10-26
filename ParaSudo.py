import paramiko

client = paramiko.SSHClient()



client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('centos',22,'test','Test!123')
client.get_transport()

command = "sudo su -c 'tail /var/log/audit/audit.log'"
stdin, stdout, stderr = client.exec_command(command=command,get_pty=True)
print("Original command sent!")
stdin.write("Test!123\n")
print("Password sent!")
stdin.flush()
print("Input flushed!")

if stderr.channel.recv_exit_status() != 0:
    print("Error occured!")
    print(f"The following error occured: {stderr.readlines()}")
else:
    print("Getting output!")
    print(f"The following output was produced: \n{stdout.readlines()}")

client.close()