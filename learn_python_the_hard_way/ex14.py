from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I am %s script" % (user_name, script)
print "I would like to ask a few questions"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s" % (user_name)
lives = raw_input(prompt)

print "what kind of computer do you have"
computer = raw_input(prompt)

print """
Alright so you said %s about liking me.
you live in %r. Not sure where that is.
and you have a %r computer. Nice.
""" % (likes, lives, computer)


