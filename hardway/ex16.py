from sys import argv
script, filename = argv
tab = '\t'

print "We're wiping file %s %s " % (tab, filename)
raw_input("Confirm with Enter or press CTRL+C")
target = open(filename,'w')
target.truncate()
rows = int(raw_input("How many lines you want into %s" % (filename)))
new_text = []
for x in range(0,rows):
    new_text.append(raw_input("Your text number %s >>" % (x+1) ))
    target.write(new_text[x])
    target.write(tab)
target.close()
reading = open(filename)
print reading.read()