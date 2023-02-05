# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#create
class User_bzt:

  # Constructor
  def __init__(self_bzt, name_bzt, email_bzt, age_bzt):
    self_bzt.name = name_bzt
    self_bzt.email = email_bzt
    self_bzt.age = age_bzt
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self_bzt._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):
      return f'My name is {self.name} and I am {self.age_bzt}'

  def has_birthday(self):
      self.age_bzt += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(User_bzt):
  # Constructor
  def __init__(self_bzt, name_bzt, email_bzt, age_bzt):
      User_bzt.__init__(self_bzt, name_bzt, email_bzt, age_bzt) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self_bzt.name = name_bzt
      self_bzt.email = email_bzt
      self_bzt.age = age_bzt
      self_bzt.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  init user object
zeynep = User_bzt('zeynep tan', 'zeynep@gmail.com', 21)
# init customer object
janet = Customer('janet johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

zeynep.has_birthday()
print(zeynep.greeting())

#encapsulation
zeynep.print_encap()
zeynep._private = 800 
zeynep.print_encap()

# method inherited from parent
janet.print_encap() 
janet._private = 600
janet.print_encap()

#similary changing janet's doesn't affect zeynep's variable
zeynep.print_encap()