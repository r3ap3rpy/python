import winrm
from pprint import pprint

Session = winrm.Session('2019B', auth = ('ansible', 'Start!12345'))
Output = Session.run_cmd('powershell',['-c','(get-eventlog -Logname Application -newest 10).Message'])

print(f"The status of the output is : {Output.status_code}")
print("#" * 50)
pprint(Output.std_out.decode().split('\r\n'))
print("#" * 50)
