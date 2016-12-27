autot = []
class auto(object):
    def __init__(self, weight, hb):
        self.weight = weight
        self.hb = hb
        
    def accelerate(self):
        return self.weight / self.hb

rounds = int(raw_input("How many cars: "))
while rounds != 0:
    rounds -= 1
    print "Still %s cars to go" % (rounds + 1)
    weight = int(raw_input("Weight?: "))
    hpb = int(raw_input("Horse Power?: "))
    autot.append(auto(weight,hpb))

for kaara in autot: 
    print "Estimated acceleration time %s seconds" % (kaara.accelerate())