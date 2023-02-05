# If/ Else conditions are used to decide to do something based on something being true or false

x_bzt = 30
y_bzt = 21


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# simple if
if x_bzt > y_bzt :
  print(f'{x_bzt} is greater than {y_bzt}')

 # if else

if x_bzt > y_bzt:
  print(f'{x_bzt} is greater than {y_bzt}')
else:
  print(f'{y_bzt} is greater than {x_bzt}') 
  
  # elif

if x_bzt > y_bzt:
  print(f'{x_bzt} is greater than {y_bzt}')
elif x_bzt == y_bzt:
  print(f'{x_bzt} is equal to {y_bzt}')  
else:
  print(f'{y_bzt} is greater than {x_bzt}')  

# nested if

if x_bzt > 2:
  if x_bzt <= 10:
    print(f'{x_bzt} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_bzt > 2 and x_bzt <= 10:
    print(f'{x_bzt} is greater than 2 and less than or equal to 10')

# or
if x_bzt > 2 or x_bzt <= 10:
    print(f'{x_bzt} is greater than 2 or less than or equal to 10')

# not
if not(x_bzt == y_bzt):
  print(f'{x_bzt} is not equal to {y_bzt}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object


#  in

numbers_bzt = [1,2,3,4,5]
if x_bzt in numbers_bzt:
  print(x_bzt in numbers_bzt)

# not in
if x_bzt not in numbers_bzt:
  print(x_bzt not in numbers_bzt)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_bzt is y_bzt:
  print(x_bzt is y_bzt)

# is not
if x_bzt is not y_bzt:
  print(x_bzt is not y_bzt)