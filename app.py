from db import init_db, insert_car, get_cars, search_cars, update_car, delete_car, get_car
from flask import Flask, request, jsonify, render_template
from flask_expects_json import expects_json

app = Flask(__name__)

init_db()

create_schema = {
    'type': 'object',
    'properties': {
        'make': {'type': 'string', "minLength": 1, "maxLength" : 100}, 
        'model': {'type': 'string', "minLength": 1, "maxLength" : 100}, 
        'color': {'type': 'string', "minLength": 1, "maxLength" : 100}, 
        'year': {'type': 'integer', "minimum": 1900, "maximum" : 2100}, 
    },
    'required': ['make', 'model', 'color', 'year']
}

search_schema = create_schema = {
    'type': 'object',
    'properties': {
        'make': {'type': 'string', "minLength": 1, "maxLength" : 100}, 
        'model': {'type': 'string', "minLength": 1, "maxLength" : 100}, 
        'color': {'type': 'string', "minLength": 1, "maxLength" : 100}, 
        'year': {'type': 'integer', "minimum": 1900, "maximum" : 2100}, 
    },
}

@app.route('/', methods=['GET'])
def get_all_cars():
    res = get_cars()
    return jsonify(res)
    
@app.route('/', methods=['POST'])
@expects_json(create_schema)
def add_car():
    data = request.json
    res = insert_car(data)
    return jsonify(res)

@app.route('/search/', methods=['GET'])
@expects_json(search_schema)
def car_search():
    res = search_cars(request.json)
    return jsonify(res)

@app.route('/<id>', methods=['GET'])
def get_single_car(id):
    res = get_car(id)
    res['id'] = id
    return jsonify(res)

@app.route('/<id>', methods=['PUT'])
@expects_json(search_schema)
def car_update(id):
    data = request.json 
    res = update_car(id, data)
    res['status'] = 'Updated'
    return jsonify(res)

@app.route('/<id>', methods=['DELETE'])
def car_delete(id):
    res = delete_car(id)
    return jsonify(res)