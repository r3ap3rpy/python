from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

information = {}

@api.route("/vault/<string:customer>")
class Vault(Resource):
    def get(self, customer):
        if not information.get(customer):
            return {"customer":"N.A."}
        else:
            return {customer : information[customer]}

    def put(self, customer):
        if not information.get(customer):
            information[customer] = {}
        for key in request.form.keys():
            information[customer].update({key:request.form[key]})

        return {customer: information[customer]}


if __name__ == '__main__':
    app.run(debug = True)
