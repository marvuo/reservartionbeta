from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

infile = open(from_file)
datafile = infile.read()

print "the %s is %r bytes long" % (from_file, len(datafile))
if exists(to_file):
    print "file to be appended"
else:
    print "will create that file for you..."
    
out_file = open(to_file,"w")
out_file.write(datafile)

infile.close()
out_file.close()
