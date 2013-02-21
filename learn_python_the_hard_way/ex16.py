from sys import argv

script, filename = argv

print "we are going to erase %r:" % filename
print "if you don't want that hit ctrl + C"
print "if you do want that hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Good Bye !"
target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I am going to write these lines to the file"

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally we close it"
target.close()



