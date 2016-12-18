states = { "New York" : "NY", "California" : "CA" }
cities = { "NY" : "New York City", "CA" : "California City" }

pnro = { "Helsinki" : "00100", "Oulu" : "90100", "Tampere" : "20100" }
kunnat ={"Uusimaa" : "Helsinki", "Pohjanmaa" : "Oulu", "Pirkanmaa" : "Tampere"}

for x in states:
    print states[x]
    
for abbrev, states in states.items():
    print "The %s stands for %s with HQ named %s" % (abbrev, states, cities[states])

print "-"*40    
for laani, kaupunki in kunnat.items():
    print "In \t %s key city is\t %s with number \t %s" % (laani, kaupunki, pnro[kaupunki])
    

print pnro[raw_input("Anna kaupunki")]