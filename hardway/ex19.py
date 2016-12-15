def cheese_crackers(boxes, cheese_per_box):
    print "We have %s boxes of cheese_crackers each with %s slices" % (boxes, cheese_per_box)
    print "Total of %r slices" % (int(boxes)*int(cheese_per_box))
    raw_input("Press enter to continue")

#slices = 7
cheese_crackers(raw_input("How many boxes you'd like >"), raw_input("Box size you'd like >"))