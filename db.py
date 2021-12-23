from elasticsearch import Elasticsearch, NotFoundError
from cars_seed import cars
# configure elasticsearch
config = {
    'host': 'host.docker.internal',
    'port': 9200
}

es = Elasticsearch([config])

index_body = {
    'settings': {
        'number_of_shards': 5,
        'number_of_replicas': 1
    },
    'mappings':
        {'dynamic': 'strict',
         'properties': {
             'make': {'type': 'text'},
             'model': {'type': 'text'},
             'color': {'type': 'text'},
             'year': {'type': 'integer'}
         }}
}

def init_db():
    try: 
        es.indices.get('cars')
    except NotFoundError:
        es.indices.create(index='cars', settings=index_body['settings'], mappings=index_body['mappings'])
        for car in cars:
            insert_car(car)

def insert_car(data):
    res = es.index(index='cars', body=data)
    return res    

def get_cars():
    res = es.search(index='cars')
    return res['hits']['hits']

def search_cars(data):
    body = {'query': {'bool':{'must': []}}}
    for key,val in data.items():
        body['query']['bool']['must'].append({'match': {key: val}})
    res = es.search(index='cars', body=body)
    return res['hits']['hits']

def get_car(id):
    res = es.get(index='cars', id=id)
    return res['_source']

def update_car(id, data):
    body = {
        'doc': data
    }
    es.update(index='cars', body=body, id=id)
    res = es.get(index='cars', id=id)
    return res['_source']

def delete_car(id):
    es.delete(index='cars', id=id)
    return {'ID': id, 'Status': 'Deleted'}

