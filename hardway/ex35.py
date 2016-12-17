from sys import exit
warrior_list = []
class Warrior(object):
    def __init__(self, warriorname, gold=0):
        self.warriorname = warriorname
        self.gold = gold
    

def start_game():
    direction = raw_input("Do you want to go to left or to the right?")
    if "left" in direction.lower():
        left_room()
    elif "right" in direction.lower():
        right_room()
    elif 'panic' in direction.lower():
        exit()
    else:
        print "Wrong direction - choose 'left' or 'right' - 'panic' to escape"
        start_game()

def left_room():
    try:
        gold_amount = int(raw_input("How much do you want to have Gold: "))
    except:
        print "must give amount in number"
        left_room()
    warrior_list[1].gold = gold_amount
    print_warriors()
    

def right_room():
    print "nothing on right  yet"
    
    
for x in range(0,5):
    myname = raw_input("Start by telling your name warrrior: ")
    warrior_list.append(Warrior(myname))

def print_warriors():
    for x in warrior_list:
        print "%s ja %s" % (x.gold, x.warriorname)

print_warriors()
start_game()