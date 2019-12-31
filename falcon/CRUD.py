from wsgiref.simple_server import make_server

import falcon

class CRUD(object):
    def on_get(self,req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Falcon GET"
    def on_put(self,req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Falcon PUT"
    def on_post(self,req, resp):
        resp.status = falcon.HTTP_201
        resp.body = "Falcon POST"

    def on_delete(self,req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Falcon DELETE"

if __name__ == '__main__':
    api = falcon.API()
    api.add_route("/", CRUD())
    with make_server('',8080, api) as api:
        api.serve_forever()
