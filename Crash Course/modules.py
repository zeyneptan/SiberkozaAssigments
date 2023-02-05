# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
from datetime import date
import time
from time import time

# pip module
from camelcase import CamelCase

# import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
# print(c.hump('hello there everyone'))

email_bzt = 'test#test.com'
if validate_email(email_bzt):
  print('email is valid')
else:
  print('email is bad')