my_list = []
def fill_list(num):
    i = 0
    while i < num:
        i += 1
        my_list.append(i)
    
fill_list(int(raw_input("From zero to: ")))
my_list[int(raw_input("""Write "Foobar" to spot: """))]  = "Foobar"



for num in my_list:
    print(num)
