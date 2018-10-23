import sanic
import subprocess

app = sanic.Sanic()

html_page = """
<H1>Welcome to the commander webapp</H1>
<p>This webapp allows you to run commands in the command and power shells.</p>
<p>You may want to use the <a href="/commander">commander endpoint</a></p>
"""

@app.route("/")
async def index(request):
	return sanic.response.html(html_page)

@app.websocket("/commander")
async def commander(request, ws):
	while True:
		data = await ws.recv()
		print("Got the input from the client: <{}>".format(data))
		if len(data.split(' ')) == 2:
			if data.split(' ')[0] in ['cmd','pshell']:
				if data.split(' ')[0] == 'cmd':
					shell = ['cmd','/c',data.split(' ')[1]]
				else:
					shell = ['powershell','-command',("& {" + data.split(' ')[1] + "}")]

				Result = subprocess.Popen(shell, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

				OK, ERR = Result.communicate()

				if not OK: OK = 'There was no output from the command!'

				await ws.send(OK)
			else:
				await ws.send("This is an invalid interpreter: <{}> it must be either <cmd> or <pshell>!".format(data.split(' ')[0]))
		else:
			await ws.send("Invalid command specified: <{}>!".format(data))


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)