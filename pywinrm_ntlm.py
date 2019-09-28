import winrm
from pprint import pprint

prot = winrm.protocol.Protocol(
        endpoint = "http://2019A:5985/wsman",
        transport = "ntlm",
        username = "ansible",
        password = "Start!12345",
        server_cert_validation = "ignore"
)

shell = prot.open_shell()

command = prot.run_command(shell, "itshouldfail")

out, err, status = prot.get_command_output(shell, command)

print(f"Errors: {err}")
print(f"Status: {status}")
pprint(f"Output: {out.decode()}")