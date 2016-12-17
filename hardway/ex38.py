ten_things = ["a","b","c","d"]
more_things = ["e","f","g","h","i","j","k","l","m"]
while len(ten_things) < 11:
    print "There are now %s things" % (len(ten_things))
    print ten_things
    ten_things.append(more_things.pop())
    