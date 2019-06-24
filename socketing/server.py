import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket demo!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

print(f"Running the server on: {args.host} and port: {args.port}")

sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	sck.bind((args.host, args.port))
	sck.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")


def on_new_client(client, connection):
	ip = connection[0]
	port = connection[1]
	print(f"THe new connection was made from IP: {ip}, and port: {port}!")
	while True:
		msg = client.recv(1024)
		if msg.decode() == 'exit':
			break
		print(f"The client said: {msg.decode()}")
		reply = f"You told me: {msg.decode()}"
		client.sendall(reply.encode('utf-8'))
	print(f"The client from ip: {ip}, and port: {port}, has gracefully diconnected!")
	client.close()

while True:
	try: 
		client, ip = sck.accept()
		threading._start_new_thread(on_new_client,(client, ip))
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!")
	except Exception as e:
		print(f"Well I did not anticipate this: {e}")

sck.close()