import subprocess

HostsOfGroup = subprocess.Popen(['/usr/bin/ansible','lin','--list-hosts'], stdout = subprocess.PIPE)
HostsOut, HostsErr = HostsOfGroup.communicate()

if HostsErr is None:
        print("No erros, good to go!")
else:
        print("The following error occured: {HostsErr}")
        raise SystemExit
ListOfHosts = []
for host in HostsOut.decode().split('\n'):
        if not "  hosts" in host:
                if host:
                        ListOfHosts.append(host.strip())

print(ListOfHosts)