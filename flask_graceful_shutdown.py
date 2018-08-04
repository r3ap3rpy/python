from flask import Flask, request

user = 'admin'
pwd = 'Start!123'

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
	return "Welcome to the flask world!"

@app.route("/shutdown", methods = ['POST'])
def shutdown_server():
	print("Shutdown context hit with POST!")
	if request.form.get('username') and request.form.get('password'):
		print('Got username: {} and password: {}'.format(request.form.get('username'),request.form.get('password')))
		if request.form.get('username') != user:
			return 'The username or password is incorrect!'

		if request.form.get('password') != pwd:
			return 'The username or password is incorrect!'

		print("It seems to be valid, the server is shutting down!")
		shutdown = request.environ.get('werkzeug.server.shutdown')
		if shutdown is None:
			raise RuntimeError('The function is unavailable!')
		else:
			shutdown()
			return "THe server is shutting down!"

	else:
		return 'You need authorization to shut the server down!'

if __name__ == '__main__':
	app.run(port = 8081, host = '0.0.0.0', debug = True)

