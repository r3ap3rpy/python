from typing import NamedTuple

class VMWareVM(NamedTuple):
	name : str
	guestOS : str
	vmHwVersion : int
	vCpu : int
	ram : int
	vmdk : int


print(VMWareVM)

Win10Guest = VMWareVM(name = 'Test VM', guestOS = 'Windows 10', vmHwVersion = 11, vCpu = 4, ram = 8, vmdk = 1)

print(Win10Guest)
print(dir(Win10Guest))
print(Win10Guest.__annotations__)
print(Win10Guest._asdict())

name, guestOS, vmHwVersion, vCpu, ram, vmdk = Win10Guest

print(name, guestOS, vmHwVersion, vCpu, ram, vmdk)