import winrm
import base64

def chunker(sequence, size):
    return (sequence[pos:pos + size] for pos in range(0,len(sequence),size))


with open('hwork.pdf','rb') as binfile:
    data = base64.b64encode(binfile.read())

Session = winrm.Session('2019B', auth=('winrm','Start!123'))

for chunk in chunker(data, 1024):
    chunk = chunk.decode()
    Result = Session.run_ps(f"'{chunk}' | Out-File -FilePath C:\\temp\\hwork.tmp -Append -NoNewline")
    print(Result.std_out)
    print(Result.std_err)

Session.run_ps("[System.Convert]::FromBase64String((Get-Content c:\\temp\\hwork.tmp)) |Set-Content -Encoding Byte -Force -Path C:\\temp\\hwork.pdf")
Session.run_ps("Remove-Item -Path c:\\temp\\hwork.tmp -Force")
