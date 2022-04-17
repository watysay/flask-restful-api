from flask import Flask
from flask_restful import Api, reqparse
from resources.helloworld import HelloWorld
from resources.myfruits import FruitsList, Fruit
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')

api.add_resource(HelloWorld, '/')
# adding fruits list
api.add_resource(FruitsList, '/fruits')
api.add_resource(Fruit, '/fruits/<fruit_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)