import json
cars = [
    {'make': 'Honda',
     'model': 'Civic',
     'color': 'Black',
     'year': 2019},
    {'make': 'Ford',
     'model': 'Taurus',
     'color': 'Red',
     'year': 2012},
    {'make': 'Toyota',
     'model': 'Carolla',
     'color': 'Blue',
     'year': 2014},
    {'make': 'Chevrolet',
     'model': 'Corvette',
     'color': 'Green',
     'year': 2010},
    {'make': 'Mitsubishi',
     'model': 'Eclipse',
     'color': 'White',
     'year': 2015},
    {'make': 'Honda',
     'model': 'CRV',
     'color': 'Yellow',
     'year': 2020},
    {'make': 'Toyota',
     'model': 'Camry',
     'color': 'Purple',
     'year': 2020},
    {'make': 'Subaru',
     'model': 'Outback',
     'color': 'Silver',
     'year': 2021},
]


print(json.dumps(cars))