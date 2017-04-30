
months = 12
arpu = float(raw_input("ARPU?: "))
saledays = int(raw_input("Sales Days per month? "))
totalmrc = []
revenuetotal = 0

while months > 0:
    months -= 1
    revenuetotal += saledays * arpu
    totalmrc.append(revenuetotal)

print revenuetotal

for id_num, mrc in enumerate(totalmrc):
    revenuetotal += mrc * (12 - (id_num))
    print mrc, 12-id_num
    print revenuetotal
    

print totalmrc