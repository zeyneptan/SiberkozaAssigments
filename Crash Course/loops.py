# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_bzt = ['zeynep', 'tan', 'sara', 'susan']

# simple for loop
for person_bzt in people_bzt:
  print(f'Current Person: {person_bzt}')

# break
for person_bzt in people_bzt:
  if person_bzt == 'sara':
    break
  print(f'Current Person_bzt: {person_bzt}')

# continue
for person_bzt in people_bzt:
  if person_bzt == 'sara':
    continue
  print(f'Current Person_bzt: {person_bzt}')

# range
for i in range(len(people_bzt)):
  print(people_bzt[i])

for i in range(0, 11):
  print(f'number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_bzt = 0
while count_bzt < 10:
  print(f'Count: {count_bzt}')
  count_bzt += 1
