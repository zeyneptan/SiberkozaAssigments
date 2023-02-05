# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


# create function
def sayHello(name_bzt='zeynep'):
    print(f'Hello {name_bzt}')


# return values
def getSum(num1_bzt, num2_bzt):
    total = num1_bzt + num2_bzt
    return total


getSum = lambda num1_bzt, num2_bzt: num1_bzt + num2_bzt

print(getSum(5, 4))

