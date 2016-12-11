from sys import argv
script, username = argv
prompt = "c:\\>"

print "Hi %s " % username
print ("Please enter your favorite command")
command = raw_input(prompt)
print "Nice %s i Prefer rm -R! See you later %s" % (command, username)