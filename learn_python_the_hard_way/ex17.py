from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# we could do these in one line or two
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" %len(indata)

print "Does the input file exist? %r : " % exists(to_file)
print "Ready. Hit enter to continue. Ctrl+C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright Done"

out_file.close()
in_file.close()





