# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods



# String Methods

from codecs import namereplace_errors
from dataclasses import replace


name_bzt = 'Zeynep'
age_bzt = 21

# concanate

print( 'Hello, my name is ' + name_bzt + ' and I am ' + str(age_bzt) )

# String Formatting

# arguments by position
print ('My name is {name} and I am {age}' .format(name=name_bzt, age=age_bzt ))

# f-strings
print ( f'Hello, my name is {name_bzt} and I am {age_bzt}')

# string methods

s_bzt = 'hello world'

# capitalize string
print(s_bzt.capitalize())

# make all uppercase
print(s_bzt.upper())

# make all lower
print(s_bzt.lower())

# swap case
print(s_bzt.swapcase())

# get lenght
print(len(s_bzt))

# replace 
print(replace('world', 'everyone'))

# count
sub = 'h'
print(s_bzt.count(sub))

# starts with
print(s_bzt.startswith('hello'))

# ends with
print(s_bzt.endswith('d'))

# split into a list
print(s_bzt.split())

# find position
print(s_bzt.find('r'))

# is all alphanumeric
print(s_bzt.isalnum())

# is all alphabetic
print(s_bzt.isalpha())

# is all numeric
print(s_bzt.isnumeric())

