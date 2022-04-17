from flask_restful import Resource


fruitlist = {
    '1' : { 'name': 'banana' },
    '2' : { 'name': 'apple' }
}

class FruitsList(Resource):
    def get(self):
        return fruitlist

class Fruit(Resource):
    def get(self, fruit_id):
        return fruitlist[fruit_id]
        