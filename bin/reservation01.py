import pickle
import datetime
import re

rcalendar = []
rcustomers = []
i = 0

class Reservation(object):
    def __init__(self, duration,idnum, calendar="00:00 00.00"):
        self.duration = duration
        self.calendar = calendar
        self.idnum = idnum

    def print_results(self):
        print("At %s to be precise" % (str(self.calendar)))

class  Customers(object):
    def __init__(self, name, idnum, email):
        self.name = name
        self.email = email
        self.idnum = idnum


def create_calendar():
    print("Format is HH:MM DD.MM")
    while True:
        try:
            requested_moment = raw_input("Requested time?")
            date_object = datetime.datetime.strptime(requested_moment, "%H:%M %d.%m")
            duration = int(input("Requested duration in minutes?"))
            print(date_object)
            rcalendar.append(Reservation(duration, date_object))
            break
        except ValueError:
            print("Oops - try again")

def manage_customer():
    i = 1
    while i != 0:
        print("What would you like to do?")
        print ("0 - Back in menu")
        print ("1- List current clients")
        print ("2 - Add new client")
        print ("3 - Remove existing client")
        print ("4 - Modify exisint client")
        i  = int(input("Valintasi?"))
        if i == 1:
            for x in rcustomers:
                print(x.idnum, x.name, x.email)
        elif i ==2:
            create_customer()
        elif i == 3:
            print ("Not yet!")
            pass
        elif i == 4:
            print ("Not yet!")
            pass
        else:
            print("Not valid choice!")



def create_customer():
    idnum = (len(rcustomers) +1)
    cust_name = raw_input("Your name: ")
    match = None
    cust_email = "Null"
    while  match == None:
        cust_email = raw_input("Your email ")
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', cust_email.lower())
        if match == None:
            print('Bad Syntax - try again ')
    rcustomers.append(Customers(cust_name,idnum,cust_email))



def resevation_slots():
    for x in rcalendar:
        #slut = datetime.datetime.strftime(((x.calendar)+ (datetime.timedelta(minutes=x.duration))),"%H:%M %d.%m")
        slut = datetime.datetime(((x.calendar)+ (datetime.timedelta(minutes=x.duration))),"%H:%M %d.%m")
        print("starting", datetime.datetime.strftime(x.calendar,"%H:%M %d.%m"), "ending", slut)



def sorting():
    a = []
    b = []
    for x in rcalendar:
        a.append(x.calendar)
    a = (sorted(a))
    for value in a:
        b.append(datetime.datetime.strftime(value,"%H:%M %d.%m"))
    return b

def total_duration():
    summa = 0
    for x in rcalendar:
        summa += x.duration
    return summa

def save_data():
    tiedosto = open("myfile.txt", "wb")
    pickle.dump(rcalendar, tiedosto)

def read_data():
    read_file = pickle.load(open("myfile.txt", "rb"))
    return read_file

def check_conflict(requested):
    free = True
    for reserved in rcalendar:
        if requested >= reserved.calendar:
            if requested < (reserved.calendar + (datetime.timedelta(minutes=reserved.duration))):
                free = False
            else:
                pass
        else:
            pass
    if free:
        print("It's free!")
    else:
        print("Sorry it's booked")
    return free

def print_times():
    for x in sorting():
        print (x)

## Body starts
# Let's iniate reservation calendar

print("Welcome to great reservation calendar!")
while i != 1:
    # print_times()
    print("---------------------------------------------------")
    print("Menu:")
    print("Lopeta painamalla            '1'")
    print("Saatavuus painamalla         '2'")
    print("Summa varauksista painamalla '3'")
    print("Tallenna painamalla          '4'")
    print("Lue tiedostoa painamalla     '5'")
    print("Tulosta data painamalla      '6'")
    print ("sort things                    '7'")
    print("Kalenteri varaus             '8'")
    print("Manage customers              '9'")

    i = int(raw_input("Valintasi:  "))

    if i == 2:
        print("Format is HH:MM DD.MM")
        requested_moment = raw_input("Requested time?")
        date_object = datetime.datetime.strptime(requested_moment, "%H:%M %d.%m")
        print(date_object)
        check_conflict(date_object)
    elif i == 3:
        print(total_duration())
    elif i == 4:
        save_data()
    elif i == 5:
        rcalendar = read_data()
    elif i == 6:
        print_times()
    elif i == 7:
        resevation_slots()
    elif i == 8:
        create_calendar()
    elif i == 9:
        manage_customer()
    else:
        pass
