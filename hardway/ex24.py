from sys import argv
scripts, foobar = argv

print "let's practice with \\ and \" printing and one tab \t like this too"
story = """\t\t There is a funny story
it goes like this has loads of tabs
and is many rows long"""

print story

print """next we're sending something to function"""

def shouting(mytext):
    #print mytext.upper()
    return mytext.upper()
    
print shouting(foobar)