x = "There are %d types of people." % 10   # this line assigns a string to the variable x and has a format character to be replace by 10
binary = "binary"
do_not = "don't"   # this line assigns a varible do_not
y = "Those who know %s and those who %s" % (binary, do_not)  #this statement defines a variable y with two format characters

print x   # this prints x
print y   #this prints y    
print "I said: %r." % x   #this prints a statement                   
print "I also said: '%s'." % y  #thissprints the staemt with a format string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r."

print joke_evaluation % hilarious

w = "This is left side of..."
e = "a string with a right side."

print w+e

