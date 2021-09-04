'''#!/usr/bin/python

# Open a file
fo = open("foo.txt", "w")
print ("Name of the file:" + fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line
fo.write("hi\n")
fo.write('welcome bye')

fo.close()
f = open("foo.txt", "r")
line = f.readline()
print ("Read Line: " + line)

line = f.readline()
print ("Read Line: " + line)


# Get the current position of the file.
pos = f.tell()
print ("Current Position: "+ str(pos))

# Close opend file
f.close()

import os
print(os.getcwd())
def insert(filename, key, value):
	f = open(filename, 'a')
	f.write(key + '\t' + value + '\n')
	f.close()
print(insert('table.txt', 'my key', 'my \t value'))
f=open('table.txt')
for line in f:
    print (line)'''
