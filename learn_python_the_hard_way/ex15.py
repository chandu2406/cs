from sys import argv

script, filename = argv

text = open(filename)

print "Here is the file %r:" % filename
print text.read()

print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

