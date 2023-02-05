# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create tuple
fruits_bzt = ('apples', 'oranges', 'grapes')

# using a constructor
# fruits_bzt2 = tuple(('apples', 'oranges', 'grapes'))

# single value needs trailing comma
fruits_bzt2 = ('apples',)

# get value
print(fruits_bzt[1])

# can't change value
fruits_bzt[0] = 'pears'

# delete tuple
del fruits_bzt2

# get length
print(len(fruits_bzt))


# set 

# create set
fruits_set_bzt = {'apples', 'oranges', 'mango'}

# check if in set
print('apples' in fruits_set_bzt)

# add to set
fruits_set_bzt.add('grape')

# remove from set
fruits_set_bzt.remove('grape')

# add duplicate
fruits_set_bzt.add('apples')

# clear set
fruits_set_bzt.clear()

# delete
del fruits_set_bzt

print(fruits_set_bzt)