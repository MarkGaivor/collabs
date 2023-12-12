capitalchik=100000
zpshka=10000
traty=20000
raznost=traty-zpshka
capitalchik=capitalchik-raznost
inflya=0.05
month=1
while capitalchik>0:
        traty*=(1+inflya)
        raznost=traty-zpshka
        capitalchik-=raznost
        month+=1
print(month-1)
