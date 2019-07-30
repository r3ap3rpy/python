from collections import OrderedDict

from flask import Flask
from flask_restplus import fields, Api, Resource

app = Flask(__name__)
api = Api(app)

model = api.model('Model',{
        'message':fields.String}
        )

class HelloWorld(object):
    def __init__(self, message):
        self.message = message

@api.route('/hello')
class Hello(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return HelloWorld(message = 'Hello To The World of Python And Flask')

if __name__ == '__main__':
    app.run(debug = True)
