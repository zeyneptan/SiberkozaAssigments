# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dictionary
person_bzt = {
    'first_name': 'zeynep',
    'last_name': 'tan',
    'age': 21 }


# use constructor
# person_bzt2 = dict(first_name='sara', last_name='williams')

# get value
print(person_bzt['first_name'])
print(person_bzt.get('last_name'))

# add key/value
person_bzt['phone'] = '555-555-5555'

# get dictionary keys
print(person_bzt.keys())

# get dictionary items
print(person_bzt.items())

# copy dictionary
person_bzt2 = person_bzt.copy()
person_bzt2['city'] = 'boston'

# remove item
del(person_bzt['age'])
person_bzt.pop('phone')

# clear
person_bzt.clear()

# get length
print(len(person_bzt2))

# list of dict
people_bzt = [
    {'name': 'martha', 'age': 30},
    {'name': 'kevin', 'age': 25}
]

print(people_bzt[1]['name'])