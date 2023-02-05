# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

userJSON_bzt = '{"first_name": "zeynep", "last_name": "tan", "age": 21}'

# parse 
user = json.loads(userJSON_bzt)

# print(user)
# print(user['first_name'])

car_bzt = {'make': 'Ford', 'model': 'mustang', 'year': 1970}

carJSON_bzt = json.dumps(car_bzt)

print(carJSON_bzt)