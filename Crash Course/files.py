# Python has functions for creating, reading, updating, and deleting files.

# open
myFile_bzt = open('myfile.txt', 'w')

# get some info
print('Name: ', myFile_bzt.name)
print('Is Closed : ', myFile_bzt.closed)
print('Opening Mode: ', myFile_bzt.mode)

# write
myFile_bzt.write('I love Python')
myFile_bzt.write(' and JavaScript')
myFile_bzt.close()

# append 
myFile_bzt = open('myfile.txt', 'a')
myFile_bzt.write(' I also like PHP')
myFile_bzt.close()

# read 
myFile_bzt = open('myfile.txt', 'r+')
text = myFile_bzt.read(100)
print(text)
