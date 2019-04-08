import socket

#get_hostbyname('name')

Resolve_Cache = {}

def resolve_ip(name):
	if Resolve_Cache.get(name):
		return f"ansible_host={Resolve_Cache[name]}"
	host_ip = None
	try:
		host_ip = socket.gethostbyname(name)
	except:
		host_ip = None
	if host_ip:
		Resolve_Cache.update({name:host_ip})
		return f"ansible_host={host_ip}"
	return ""