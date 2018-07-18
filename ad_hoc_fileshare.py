import http.server
import os
import sys

Program, Port, Folder = sys.argv

try:
	http.server.HTTPServer(("",int(Port)),http.server.SimpleHTTPRequestHandler).serve_forever()
except KeyboardInterrupt:
	daemon.socket.close()