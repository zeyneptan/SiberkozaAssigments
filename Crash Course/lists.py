# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers_bzt = [1, 2, 3, 4, 5]
fruits_bzt = ['apples', 'oranges', 'grapes', 'pears']

# use a constructor
# numbers2_bzt = list((1, 2, 3, 4, 5))

# get a value
print(fruits_bzt[1])

# get the last value
print(fruits_bzt[-1])



# get length
print(len(fruits_bzt))

# append to list
fruits_bzt.append('mangos')

# remove from list
fruits_bzt.remove('grapes')

# insert into position
fruits_bzt.insert(2, 'strawberries')

# change value
fruits_bzt[0] = 'blueberries'

# remove with pop
fruits_bzt.pop(2)

# reverse list
fruits_bzt.reverse()

# sort list
fruits_bzt.sort()

# reverse sort
fruits_bzt.sort(reverse=True)

print(fruits_bzt) 