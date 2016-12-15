from sys import argv
script, input_filename = argv
num = 1
def print_all(filename):
    print open(filename).read()
    
def print_line_skippted(filename):
    num = int(raw_input("Which line number?"))
    print open(filename).readline(num)

def seek(filename):
    print "seek"
    print open(filename).seek(0)
    
    
def print_line(filename, lines):
    print  lines, open(filename).readline()
    print  lines+1, open(filename).readline()
    
print_all(input_filename)
seek(input_filename)
print_line_skippted(input_filename)
print_line(input_filename, num)

## There is some hickup not to print lines one by one...

