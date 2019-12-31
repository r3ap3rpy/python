from wsgiref.simple_server import make_server

import falcon

class HelloWorld(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello Wolrd"

class HelloWorldJson(object):
    def on_get(self, req, resp):
        resp.media = {'response' : 'Hello World'}

if __name__ == '__main__':
    api = falcon.API()
    api.add_route('/',HelloWorld())
    api.add_route('/json',HelloWorldJson())
    
    with make_server('',8080, api) as httpd:
        httpd.serve_forever()
