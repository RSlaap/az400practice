# Very simple webapp to test in container
from json import load
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from marshmallow import Schema, fields
app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Stephan')
def stephan():
    return render_template('stephan.html')


@app.route('/Rapha')
def rapha():
    return render_template('rapha.html')


class APISchema(Schema):
    # Ill figure this out some other time
    # f = open('static/crazy_data.json')
    # data = load(f)
    # data = { "Stephan": "Gek", "Reijer": "Gekker", "Jolan": "Gekst"}
    name = fields.Str(required=True)
    # value = data[name]
    
class API(Resource):
    def get(self):
        # Klote marshmallow
        schema = APISchema()
        errors = schema.validate(request.args)
        if errors:
            return "What is your name? Get request is from the wrong format. Format is: /api?name=<name>", 400
        data = { "Stephan": "Gek", "Reijer": "Gekker", "Jolan": "Gekst", "Roman": "Cool"}
        return data[request.args['name']], 200
api.add_resource(API, '/api')
