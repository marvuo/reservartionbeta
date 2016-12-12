from sys import argv
script, filename = argv

txt = open(filename)
print "We're opening file %s" % filename
print txt.read()
txt_again = open(raw_input("I'm asking you to repeat the filename:> "))
print txt_again.read()