zpshka=20000
traty=25000
capitalchik=traty-zpshka
inflya=0.03
for i in range(2,10):
    traty*=(1+inflya)
    capitalchik += traty - zpshka
print(round(capitalchik,2))

