capitalchik=89203918
zpshka=237821
traty=2123942
my_denezhki=capitalchik+zpshka-traty
inflya=0.05
month=1
while my_denezhki>0:
        my_denezhki-=traty*(1+inflya)
        month+=1
print(month)