from sys import argv
script, filename = argv

class participant(object):
    def __init__(self, name, vegan, milk, peanut):
        self.name = name
        self.vegan = vegan
        self.milk = milk
    def fingerprint(self):
       
        return self.name
        
participants = []

raw_data = []
source = open(filename)
headers = []

for line in source:
    headers.append(line.strip().split(";")[::1])
    break

print headers

for line in (source):
    a = line.strip().split(";")[::-1]
    raw_data.append(a[:7])


fingerprints = []

for item in raw_data:
    fingerprints.append(''.join(item))

myset = set(fingerprints)

print fingerprints

diet_count = {}
for x in myset:
    diet_count[x] = fingerprints.count(x)
print diet_count



diets =[]

vegan = 0
for retard in participants:
    vegan += retard.vegan
    diets.append(retard.fingerprint())

#print Simo.fingerprint()


print "Vegan count %s" % (vegan)
print diets



